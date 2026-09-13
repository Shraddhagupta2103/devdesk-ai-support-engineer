from pathlib import Path


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


def chunk_text(text, chunk_size=500, overlap=50):

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


if __name__ == "__main__":

    documents = load_documents()

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

    print(
        f"Loaded documents: {len(documents)}"
    )

    print(
        f"Total chunks: {len(all_chunks)}"
    )

    print("\nFirst chunk:\n")

    print(
        all_chunks[0]["text"]
    )