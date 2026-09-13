from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


ESCALATION_SCENARIOS = [
    # Security
    "The customer reports a security vulnerability or security breach.",
    "The customer reports unauthorized access to their account.",
    "The customer's account has been hacked or compromised.",
    "Someone has gained unauthorized access to the customer's account.",

    # Data loss
    "The customer reports that customer data has been deleted or lost.",
    "The customer's data has disappeared.",
    "The customer reports missing customer records.",
    "The customer's data is corrupted or damaged.",

    # Outage
    "The customer reports a platform-wide service outage.",
    "Multiple services are unavailable.",
    "The entire platform appears to be down.",
]


escalation_embeddings = model.encode(
    ESCALATION_SCENARIOS
)


def should_escalate(
    question,
    threshold=0.55
):
    """
    Determine whether a customer question is
    semantically similar to an escalation scenario.
    """

    question_embedding = model.encode(
        [question]
    )

    similarities = cosine_similarity(
        question_embedding,
        escalation_embeddings
    )[0]

    best_score = similarities.max()

    return bool(
        best_score >= threshold
    )