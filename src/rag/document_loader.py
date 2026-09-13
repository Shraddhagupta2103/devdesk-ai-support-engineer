from pathlib import Path


# Location of our knowledge base
DOCUMENTS_DIR = Path(
    r"C:\Users\Smart-Computer\PycharmProjects\ai-support-engineer\scripts\data"
)


def load_documents():
    """
    Load all Markdown documents from the knowledge base.
    """

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


if __name__ == "__main__":

    documents = load_documents()

    print(f"Loaded {len(documents)} documents.")

    for document in documents:

        print(f"- {document['source']}")