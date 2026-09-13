from pathlib import Path
import pickle

import faiss
from sentence_transformers import SentenceTransformer


# Your data folder
DOCUMENTS_DIR = Path(
    r"C:\Users\Smart-Computer\PycharmProjects\ai-support-engineer\scripts\data"
)

# Where we will save the vector database
VECTOR_STORE_DIR = DOCUMENTS_DIR / "vector_store"
VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)


def load_documents():
    documents = []

    for file_path in DOCUMENTS_DIR.rglob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": str(file_path),
            "text": text
        })

    return documents


def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_chunks(documents):
    all_chunks = []

    for document in documents:

        chunks = chunk_text(document["text"])

        for chunk in chunks:

            all_chunks.append({
                "source": document["source"],
                "text": chunk
            })

    return all_chunks


if __name__ == "__main__":

    print("Loading documents...")

    documents = load_documents()

    print(f"Documents loaded: {len(documents)}")


    print("Creating chunks...")

    chunks = create_chunks(documents)

    print(f"Chunks created: {len(chunks)}")


    print("Loading embedding model...")

    model = SentenceTransformer("all-MiniLM-L6-v2")


    print("Creating embeddings...")

    embeddings = model.encode(
        [chunk["text"] for chunk in chunks],
        show_progress_bar=True
    )


    print("Creating FAISS index...")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)


    print(f"Vectors stored in FAISS: {index.ntotal}")


    print("Saving FAISS index...")

    faiss.write_index(
        index,
        str(VECTOR_STORE_DIR / "index.faiss")
    )


    print("Saving chunks...")

    with open(
        VECTOR_STORE_DIR / "chunks.pkl",
        "wb"
    ) as file:

        pickle.dump(chunks, file)


    print("\nVector store created successfully!")