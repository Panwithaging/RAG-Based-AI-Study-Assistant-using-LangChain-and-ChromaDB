from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
import chromadb
from tempfile import NamedTemporaryFile

embed_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

DIR_PATH=Path("./DATA")
client=chromadb.PersistentClient(path=DIR_PATH)

def check_collection(cn):
    collections=client.list_collections()
    exists=any(
        collection.name==cn
        for collection in collections 
    )
    return exists

def create_collection(file,collection_name):
    #collection_name=input("Enter collection name:")
    if check_collection(collection_name):
        return False , f"{collection_name} Already exists"

    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.getvalue())
        temp_path = tmp.name

    
    loader=PyPDFLoader(temp_path)
    pages=loader.load()
        
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
        )
    chunks=text_splitter.split_documents(pages)
        
    Chroma.from_documents(
        documents=chunks,
        embedding=embed_model,
        collection_name=collection_name,
        persist_directory=str(DIR_PATH)
        )
        
    return True, f"Succesfully stored {len(chunks)} chunk in database"


def del_collection(collection_name):
    if not check_collection(collection_name):
        return False, f"{collection_name} does not exist"
    client.delete_collection(name=collection_name)
    return True,f"{collection_name} deleted sucessfully"

def list_collections():
    collections=client.list_collections()
    return [collection.name for collection in collections]

if __name__=="__main__":
    book_path=Path("book/mml-book.pdf")
    #create_collection(book_path)
    list_collections()