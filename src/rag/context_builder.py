def build_context(documents):
    """
    Combine retrieved documents into a single context
    that can be provided to the LLM.
    """

    context_parts = []

    for i, document in enumerate(documents, start=1):

        context_parts.append(
            f"""
Source {i}: {document['source']}

{document['text']}
"""
        )

    return "\n".join(context_parts)