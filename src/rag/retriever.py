from pathlib import Path
import pickle

import faiss
from sentence_transformers import SentenceTransformer


# Your vector store path
VECTOR_STORE_DIR = Path(
    r"C:\Users\Smart-Computer\PycharmProjects\ai-support-engineer\scripts\data\vector_store"
)


print("Loading FAISS index...")

index = faiss.read_index(
    str(VECTOR_STORE_DIR / "index.faiss")
)


print("Loading chunks...")

with open(
    VECTOR_STORE_DIR / "chunks.pkl",
    "rb"
) as file:

    chunks = pickle.load(file)


print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_documents(query, top_k=3):

    # Convert user question into an embedding
    query_embedding = model.encode(
        [query]
    )

    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_id in zip(distances[0], indices[0]):

        results.append({
            "text": chunks[index_id]["text"],
            "source": chunks[index_id]["source"],
            "distance": float(distance)
        })

    return results


