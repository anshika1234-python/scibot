import pickle
import faiss
import numpy as np
from llama_cpp import Llama
from langchain.embeddings import HuggingFaceEmbeddings

INDEX_FILE = "faiss_index.idx"
DOCS_FILE = "faiss_docs.pkl"

print("Loading FAISS index & documents...")
index = faiss.read_index(INDEX_FILE)
with open(DOCS_FILE, "rb") as f:
    documents = pickle.load(f)

print("Loading embedding model...")
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Loading local LLM model...")
llm = Llama(model_path="models/phi-2.gguf", n_ctx=2048)

def search_and_chat(query, k=3):
    query_vec = np.array([embedding_model.embed_query(query)], dtype="float32")
    D, I = index.search(query_vec, k)
    context = "\n".join([documents[i] for i in I[0]])

    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    output = llm(prompt, max_tokens=256, stop=["\n", "User:"], echo=False)
    return output["choices"][0]["text"].strip()

if __name__ == "__main__":
    while True:
        q = input("\nAsk: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("\nAnswer:", search_and_chat(q))
