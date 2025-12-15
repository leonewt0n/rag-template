import streamlit as st
import backend as rag

st.title("Recommendation System with RAG Pipeline")
st.subheader("Add a subheader with more explanation if you want")
st.divider()

# Create a sidebar
# Upload in here the context that goes into MongoDB (knowledge base)
with st.sidebar:
    st.header("Upload context")
    user_text = st.text_area("Enter knowledge here", height=150)

    if st.button("Upload to MongoDB"):
        if user_text:
            with st.spinner("Processisng"):
                rag.ingest_text(user_text)
                st.success("Uploaded")
        else:
            st.warning("Please enter text")

