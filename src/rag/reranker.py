from sentence_transformers import CrossEncoder


# Reranking model
model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_documents(query, documents, top_k=3):
    """
    Rerank retrieved documents based on
    how relevant they are to the user query.
    """

    pairs = []

    for document in documents:
        pairs.append(
            [query, document["text"]]
        )

    scores = model.predict(pairs)

    reranked_documents = []

    for document, score in zip(documents, scores):

        reranked_documents.append({
            "text": document["text"],
            "source": document["source"],
            "score": float(score)
        })

    reranked_documents.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return reranked_documents[:top_k]