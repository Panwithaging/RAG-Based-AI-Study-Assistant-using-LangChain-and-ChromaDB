import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from langchain_manager import create_collection,del_collection,list_collections

st.title("Document upload")
st.caption("Upload PDFs to build your personal AI knowledge base.")

select=st.selectbox("Select your action",["Upload","Delete","List"],filter_mode=None,index=None,placeholder="Select a action")


if select=="Upload":
    with st.container(border=True):
        collection_name=st.text_input("Enter your PDF name:")
        collection_name=collection_name.replace(" ","-")
        uploaded_file=st.file_uploader(
                        "Drag and drop ur PDF file here",
            type=["pdf"]
            )
        s1=st.button("Upload")
        if s1:
            if not collection_name.strip() or uploaded_file is None:
                st.error("pls enter the name and upload file")
            else:
                success,message=create_collection(uploaded_file,collection_name)
                if success:
                    st.success(message)
                else:
                    st.error(message)    
elif select=="Delete":
    with st.container(border=True):
        collection=list_collections()
        collection_name=st.selectbox("Select the document",collection)
        collection_name=collection_name.replace(" ","-")
        s2=st.button("Delete")
        if s2:
            if not collection_name.strip():
                st.error("pls enter the collection name!")
            else:
                success,message=del_collection(collection_name)
                if success:
                    st.success(message)
                else:
                    st.error(message)
elif select=="List":
    with st.container(border=True):
        s3=st.button("show")
        if s3:
            collections=list_collections()

            if collections:
                st.subheader("Available collections")

                for collection in collections:
                    st.write(f"->{collection}")

            else:
                st.info("No collection found")


    