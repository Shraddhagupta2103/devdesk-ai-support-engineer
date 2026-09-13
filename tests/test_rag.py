from src.rag.rag_pipeline import search_knowledge_base


question = input("Enter your question: ")

results = search_knowledge_base(
    question,
    retrieve_k=10,
    rerank_k=3
)

print("\nTop relevant documents:\n")

for i, result in enumerate(results, start=1):

    print(f"--- Result {i} ---")
    print(f"Source: {result['source']}")
    print(f"Score: {result['score']:.4f}")
    print(f"Text: {result['text'][:500]}")
    print()