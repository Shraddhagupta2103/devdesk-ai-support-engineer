from pathlib import Path

from sentence_transformers import SentenceTransformer

DOCUMENTS_DIR = Path(
    r"C:\Users\Smart-Computer\PycharmProjects\ai-support-engineer\scripts\data"
)



def load_documents():

    documents = []

    for file_path in DOCUMENTS_DIR.rglob("*.md"):

        text = file_path.read_text(
            encoding="utf-8"
        )

        documents.append({
            "source": str(file_path),
            "text": text
        })

    return documents


def chunk_text(
    text,
    chunk_size=500,
    overlap=50
):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_chunks(documents):

    all_chunks = []

    for document in documents:

        chunks = chunk_text(
            document["text"]
        )

        for chunk in chunks:

            all_chunks.append({
                "source": document["source"],
                "text": chunk
            })

    return all_chunks


if __name__ == "__main__":

    print("Loading documents...")

    documents = load_documents()

    print(
        f"Documents loaded: {len(documents)}"
    )

    print("Creating chunks...")

    chunks = create_chunks(
        documents
    )

    print(
        f"Chunks created: {len(chunks)}"
    )

    print("Loading embedding model...")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    print("Creating embeddings...")

    embeddings = model.encode(
        [chunk["text"] for chunk in chunks],
        show_progress_bar=True
    )

    print(
        f"Embedding shape: {embeddings.shape}"
    )