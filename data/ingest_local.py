import os
import pickle
import faiss
import numpy as np
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from tqdm import tqdm

DATA_DIR = "documents"
INDEX_FILE = "faiss_index.idx"
DOCS_FILE = "faiss_docs.pkl"

print("Loading embedding model...")
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

documents = []
print(f"Loading documents from {DATA_DIR}...")
for file in tqdm(os.listdir(DATA_DIR)):
    path = os.path.join(DATA_DIR, file)
    if file.lower().endswith(".txt"):
        loader = TextLoader(path)
        docs = loader.load()
    elif file.lower().endswith(".pdf"):
        loader = PyPDFLoader(path)
        docs = loader.load()
    else:
        continue
    documents.extend(docs)

print("Splitting documents...")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)
texts = [d.page_content for d in docs]

print("Creating embeddings...")
embeddings = embedding_model.embed_documents(texts)
embeddings = np.array(embeddings).astype("float32")

print("Building FAISS index...")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, INDEX_FILE)
with open(DOCS_FILE, "wb") as f:
    pickle.dump(texts, f)

print(f"✅ Ingestion complete! {len(texts)} chunks stored.")
