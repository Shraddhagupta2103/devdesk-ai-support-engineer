from src.rag.retriever import retrieve_documents
from src.rag.reranker import rerank_documents
from src.rag.context_builder import build_context


def search_knowledge_base(query, retrieve_k=10, rerank_k=3):
    """
    Retrieve relevant documents using FAISS,
    rerank them, and build the final context.
    """

    # Step 1: Retrieve candidate documents
    retrieved_documents = retrieve_documents(
        query,
        top_k=retrieve_k
    )

    # Step 2: Rerank the candidates
    reranked_documents = rerank_documents(
        query,
        retrieved_documents,
        top_k=rerank_k
    )

    # Step 3: Build context for the LLM
    context = build_context(
        reranked_documents
    )

    return context, reranked_documents