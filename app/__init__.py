"""
App Package Initialization

This package contains the main application logic, including:
- `st_app`: The Streamlit application entry point.
- `qa_model`: Functions for querying models and handling fallback logic.
- `doc_processing`: Functions for PDF processing and database management.
- `utils`: Miscellaneous helper functions.
"""

from .st_app import main
from .qa_model import load_models, get_answer_with_fallback
from .doc_processing import process_pdf, create_in_memory_database

__all__ = [
    "main",
    "load_models",
    "get_answer_with_fallback",
    "process_pdf",
    "create_in_memory_database",
]
