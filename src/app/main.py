import streamlit as st

st.set_page_config(page_title="AI Student assistance",layout="wide")

pg=st.navigation(
    [
        st.Page("home.py",title="Home"),
        st.Page("doc.py",title="Doc"),
        st.Page("chat.py",title="Chat"),
    ]
)

pg.run()