from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv
from pathlib import Path
import os
import streamlit as at

load_dotenv()
groq_api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    api_key=groq_api_key,
    model="openai/gpt-oss-120b",
    temperature=0.1,
    max_tokens=1024,
    timeout=60,
    max_retries=3
)

DIR_PATH=Path("./DATA")

embed_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

prompt = ChatPromptTemplate.from_template("""
        You are a helpful student assistant.

        Use ONLY the context below to answer the user's question.
        If the answer is not found in the context, say:
        "I couldn't find that information in the uploaded documents."

        Context:
        {context}

        Question:
        {question}

        Answer:
    """)

parser=StrOutputParser()

def QA(collection_name,user_input):
    #user_input=input("Enter your question:")
    vector_store=Chroma(
        collection_name=collection_name,
        persist_directory=str(DIR_PATH),
        embedding_function=embed_model
    )

    retriever=vector_store.as_retriever(
        search_kwargs={"k":4}
    )
   
    docs=retriever.invoke(user_input)
    if not docs:
        return "I couldn't find any relevant information in the selected collection."
    
    
    context="\n\n".join(doc.page_content for doc in docs)

    prompt_value=prompt.invoke(
        {
            "context":context,
            "question":user_input
        }
    )

    response=llm.invoke(prompt_value)

    answer=parser.invoke(response)


    return answer

if __name__=="__main__":
    print(QA("math_for_ml"))
    
