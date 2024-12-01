from langchain_chroma import Chroma
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain.schema import Document

# Initialize embedding model
embedding_model = OllamaEmbeddings(model="llama3.1", base_url="http://127.0.0.1:11434")

@st.cache_data
def process_pdf(uploaded_file):
    """Extract and split text from the uploaded PDF."""
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks

    
    from langchain.schema import Document
from chromadb.config import Settings
import tempfile

# Global variables for Chroma instance and temporary directory
_chroma_instance = None
_temp_dir = None

def create_in_memory_database(text_chunks=None):
    """Create or retrieve a singleton in-memory Chroma database."""
    global _chroma_instance, _temp_dir

    # If an instance already exists, reuse it
    if _chroma_instance is not None:
        return _chroma_instance, _temp_dir

    # Create a temporary directory for storage
    _temp_dir = tempfile.TemporaryDirectory()

    # Configure Chroma to use the temporary directory
    temp_settings = Settings(
        persist_directory=_temp_dir.name  # Use the temporary directory
    )

    # Initialize the Chroma database
    _chroma_instance = Chroma(embedding_function=embedding_model, client_settings=temp_settings)

    # If text_chunks are provided, add them to the database
    if text_chunks:
        try:
            # Convert chunks into Document objects
            documents = [
                Document(page_content=chunk, metadata={"id": f"doc-{i}"})
                for i, chunk in enumerate(text_chunks)
            ]
            _chroma_instance.add_documents(documents)
            print(f"Added {len(documents)} documents to the database.")

            # Test the database using similarity_search
            test_query = "dummy test query"
            results = _chroma_instance.similarity_search(test_query, k=1)
            if not results:
                print("No results found in the database during test query.")
            else:
                print(f"Database test passed with {len(results)} result(s).")

        except Exception as e:
            print(f"Database error detected: {e}. Reinitializing...")

            # Reinitialize the database
            _temp_dir.cleanup()  # Clean up the temporary directory
            return create_in_memory_database(text_chunks)

    return _chroma_instance, _temp_dir
