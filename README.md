# scibot
# AI Text Search Chatbot

![Project Logo](https://yourdomain.com/logo.png)  <!-- Optional: add your logo URL -->

## Overview

This project is a lightweight AI-powered chatbot designed for fast, local semantic search over text documents without relying on external API keys or cloud services. It uses small, efficient HuggingFace models to embed and index documents, enabling quick retrieval and conversational querying.

Built with Python, LangChain, FAISS, and Streamlit, the chatbot is perfect for knowledge bases, documentation assistants, or any project requiring natural language search over textual data.

---

## Features

- **Local embeddings** using small HuggingFace models (no external API key needed)
- Fast similarity search with FAISS vector indexing
- Easy ingestion of plain text documents
- Interactive web UI built with Streamlit
- Extendable: add your own documents to enhance knowledge base
- Lightweight and fast, suitable for resource-limited environments

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ai-text-search-chatbot.git
   cd ai-text-search-chatbot
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your .txt documents into the documents/ folder.

Ingest documents to create the vector index:

bash
Copy
Edit
python ingest_local.py
Run the chatbot app:

bash
Copy
Edit
streamlit run app.py
Open the URL shown in the terminal (usually http://localhost:8501).

Project Structure
graphql
Copy
Edit
├── app.py                # Streamlit app to run the chatbot UI
├── ingest_local.py       # Script to load documents and build FAISS index
├── documents/            # Folder containing text files to index
├── model/                # Folder to store downloaded HuggingFace models
├── requirements.txt      # Python dependencies
└── README.md             # This file
Usage
Add or update .txt files in the documents/ folder.

Re-run ingest_local.py to update the FAISS index.

Use the chatbot UI to ask questions or search your documents conversationally.

Technologies Used
Python 3.8+

LangChain

FAISS

HuggingFace Transformers

Streamlit

Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues or submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

