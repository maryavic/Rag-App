#from langchain_ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from transformers import pipeline
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM

def load_models():
    """Load multiple models for answering questions."""
    models = {
        "LLaMA 3.1": OllamaLLM(model="llama3.1", base_url="http://127.0.0.1:11434"),
        "GPT": pipeline("text-generation", model="EleutherAI/gpt-neo-125M"),
        "Gemma": pipeline("text-generation", model="facebook/opt-350m"),
    }
    return models


from langchain.schema import Document

def get_answer_with_fallback(query, db, model):
    """Query the database and fallback to the model's general knowledge if needed."""
    try:
        # Check if the database has any documents
        all_docs = db.get_all_documents()
        if not all_docs:
            return "The database is empty. Please upload a PDF to add content."

        # Perform a similarity search in the Chroma database
        results = db.similarity_search(query, k=5)

        # Combine the retrieved context
        context = "\n\n".join([doc.page_content for doc in results])

        # If no relevant context is found, fallback to the model
        if not context:
            return model.invoke(query)

        # Define the prompt for the model
        prompt = f"""
        Based on the following context, answer the question:
        {context}

        Question: {query}
        """
        return model.invoke(prompt)
    except Exception as e:
        # Log and return the error
        print(f"Error during answer generation: {e}")
        return f"An error occurred: {e}"
