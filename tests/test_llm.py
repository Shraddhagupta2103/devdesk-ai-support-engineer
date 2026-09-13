from src.rag.rag_pipeline import search_knowledge_base
from src.llm.llm_client import generate_answer


question = input("Enter your question: ")


# Retrieve relevant knowledge
context, documents = search_knowledge_base(
    question
)


# Generate answer
answer = generate_answer(
    question,
    context
)


print("\nAI Support Engineer:\n")
print(answer)


print("\nSources:\n")

for i, document in enumerate(documents, start=1):

    print(f"{i}. {document['source']}")