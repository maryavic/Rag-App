from setuptools import setup, find_packages

setup(
    name="Rag_App",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "langchain",
        "chromadb",
        "transformers",
        "PyPDF2",
        "langchain_ollama",
        "duckdb",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
