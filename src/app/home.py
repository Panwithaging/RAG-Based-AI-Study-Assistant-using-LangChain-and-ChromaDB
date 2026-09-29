import streamlit as st


st.title("AI STUDY ASSISTANCE")
st.subheader("Learn smarter with AI. Upload your study materials, ask questions, and get answers grounded in your own documents.")

st.write("---")

col1,col2=st.columns(2)

with col1:
    with st.container(border=True):
        #st.image("images/chatbot.png", use_container_width=True)
        st.subheader("AI Chat")
        st.write("Ask questions from your uploaded study materials.")

with col2:
    with st.container(border=True):
        #st.image("images/pdf.png", use_container_width=True)
        st.subheader("PDF Upload")
        st.write("Upload books, notes and lecture PDFs.")
st.write("---")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        #st.image("images/search.png", use_container_width=True)
        st.subheader("Semantic Search")
        st.write("""
        Sentence Transformers,ChromaDB,Top-k Retrieval,Context-based Answers""")

with col4:
    with st.container(border=True):
        #st.image("images/ai.png", use_container_width=True)
        st.subheader("AI Models")
        st.write("""HuggingFace Embeddings,Groq API,LangChain,RAG Pipeline""")


st.divider()

st.header("Upcoming Features")

with st.container(border=True):
    st.markdown("""
    - DOCX Support
    - PPTX Support
    - Conversation History
    - Authentication
    - OCR for Images
    - Voice Input
    - Flashcard Generator
    - Quiz Generator
    - Notes Summarizer
    """)

st.divider()

st.header("Connect")
with st.container(border=True):
    st.markdown("""
    **GitHub:** https://github.com/Panwithaging

    **LinkedIn:** https://www.linkedin.com/in/pangingtushar54/

    **Email:** pangingtushar54@gmail.com
    """)