import streamlit as st
from app.doc_processing import process_pdf, create_in_memory_database
from qa_model import get_answer_with_fallback, load_models

# Load available models
models = load_models()
model_choices = list(models.keys())

st.title("Ask Me About Your PDF or Anything Else")

# Upload PDF
st.header("Upload Your PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

db = None  # Initialize the database as None

if uploaded_file:
    st.write("Processing PDF...")
    text_chunks = process_pdf(uploaded_file)

    # Clear and recreate the database with new text_chunks
    db, temp_dir = create_in_memory_database(text_chunks)
    st.success("PDF content has been processed and added to the in-memory database.")



# Model Selection
st.header("Select a Model")
selected_model = st.selectbox("Choose a model:", model_choices)

# Query Input
st.header("Ask a Question")
query = st.text_input("Enter your question here")

if st.button("Get Answer"):
    if query:
        # Reuse the existing Chroma database instance
        db, _ = create_in_memory_database()
        answer = get_answer_with_fallback(query, db, models[selected_model])
        st.write("Answer:")
        st.write(answer)
    else:
        st.error("Please enter a question!")
