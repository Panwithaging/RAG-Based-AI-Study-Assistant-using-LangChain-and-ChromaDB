import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from langchain_manager import list_collections
from QA import QA

st.title("AI Study Assistant")
st.caption("Ask questions about your uploaded documents")

collections=list_collections()

collection=st.selectbox("Select the document",collections,index=None,placeholder="Choose a document")


if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if collection:
    collection=collection.replace(" ","-")
    prompt=st.chat_input("Ask your question")

    if prompt:
        st.session_state.messages.append(
            {"role":"user",
            "content":prompt}
            )
                    
        with st.chat_message("user"):
            st.markdown(prompt)
                    
        with st.spinner("Thinking......"):
            answer=QA(collection,prompt)
                    
        with st.chat_message("assistant"):
            st.markdown(answer)
                    
        st.session_state.messages.append(
            {"role":"assistant",
            "content":answer}
            )