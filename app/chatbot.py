import sys
from pathlib import Path

import streamlit as st


# --------------------------------------------------
# Project path
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.rag.rag_pipeline import search_knowledge_base
from src.rag.semantic_escalation import should_escalate
from src.llm.llm_client import generate_answer


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="DevDesk AI Support Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# Custom styling
# IMPORTANT:
# No fixed theme colors for the app/chat.
# Streamlit controls light/dark theme colors.
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* ------------------------------------------
       Main layout
       ------------------------------------------ */

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }


    /* ------------------------------------------
       Header
       This is intentionally fixed because it is
       a branded component.
       ------------------------------------------ */
       
    .main-header {
        background: #173b7a;
        

        padding: 32px 32px;
        border-radius: 18px;
        margin-bottom: 25px;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.12);
    }
    
    
    .main-title {
        margin: 0 !important;
        font-size: 32px !important;
        line-height: 1.2 !important;
        font-weight: 750 !important;
        color: #ffffff !important;
        font.align: bottom;
    }

    .main-subtitle {
        margin-top: 9px !important;
        margin-bottom: 0 !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
        color: #e0f2fe !important;
        font.align: bottom
    }

    '''
    .main-header h1 {
        margin: 0;
        font-size: 32px;
        font-weight: 700;
        color: white;
    }
    '''
    .main-header p {
        margin-top: 8px;
        margin-bottom: 0;
        font-size: 16px;
        color: white;
        opacity: 0.9;
    }


    /* ------------------------------------------
       Chat messages
       Do NOT set color/background here.
       Streamlit handles both themes.
       ------------------------------------------ */

    div[data-testid="stChatMessage"] {
        border-radius: 14px;
        margin-bottom: 12px;
    }


    /* ------------------------------------------
       Chat input
       No fixed colors.
       ------------------------------------------ */

    div[data-testid="stChatInput"] {
        border-radius: 14px;
    }


    /* ------------------------------------------
       Sources
       No fixed background/text colors.
       Streamlit theme handles them.
       ------------------------------------------ */

    .source-box {
        border-left: 4px solid #2457a6;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 8px;
    }


    /* ------------------------------------------
       Escalation box
       Use Streamlit alert instead of a custom
       fixed-color box so it adapts to the theme.
       ------------------------------------------ */

    .escalation-box {
        border-left: 5px solid #e67e22;
        padding: 16px;
        border-radius: 10px;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    """
    <div class="main-header">
        <div class="main-title">🤖 DevDesk AI Support Engineer</div>
        <div class="main-subtitle">
            AI-powered technical support using semantic search, RAG, reranking and Gemini.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Conversation history
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )

        sources = message.get(
            "sources",
            []
        )

        if sources:

            with st.expander(
                "📚 View Sources"
            ):

                for source in sources:

                    st.markdown(
                        f"""
                        <div class="source-box">
                            {source}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


# --------------------------------------------------
# User input
# --------------------------------------------------

question = st.chat_input(
    "Describe your technical issue..."
)


# --------------------------------------------------
# Process question
# --------------------------------------------------

if question:

    # ----------------------------------------------
    # Store user message
    # ----------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):

        st.markdown(
            question
        )


    # ----------------------------------------------
    # Assistant response
    # ----------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Analyzing your issue..."
        ):

            # ------------------------------------------
            # 1. Semantic escalation
            # ------------------------------------------

            if should_escalate(question):
                response = (
                    "Your issue has been escalated to human support. "
                    "A DevDesk support engineer will assist you within 24 hours."
                )

                st.markdown(
                    f"🚨 **Human Support Recommended**\n\n{response}"
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                        "sources": []
                    }
                )

                st.stop()



            # ------------------------------------------
            # 2. Retrieve + rerank
            # ------------------------------------------

            context, documents = (
                search_knowledge_base(
                    question
                )
            )


            # ------------------------------------------
            # 3. Insufficient knowledge
            # ------------------------------------------

            if context is None:

                response = (
                    "I don't have enough relevant "
                    "documentation to answer this "
                    "confidently. I recommend escalating "
                    "this issue to a human support engineer."
                )

                st.warning(
                    f"⚠️ {response}"
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                        "sources": []
                    }
                )

                st.stop()


            # ------------------------------------------
            # 4. Generate answer
            # ------------------------------------------

            try:

                answer = generate_answer(
                    question,
                    context
                )

            except Exception:

                answer = (
                    "I was unable to generate a response "
                    "at the moment. Please try again later."
                )


            # ------------------------------------------
            # 5. Display answer
            # ------------------------------------------

            st.markdown(
                answer
            )


            # ------------------------------------------
            # 6. Collect sources
            # ------------------------------------------

            sources = []

            for document in documents:

                source = document["source"]

                if source not in sources:

                    sources.append(
                        source
                    )


            # ------------------------------------------
            # 7. Display sources
            # ------------------------------------------

            if sources:

                with st.expander(
                    "📚 View Sources"
                ):

                    for source in sources:

                        st.markdown(
                            f"""
                            <div class="source-box">
                                {source}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


            # ------------------------------------------
            # 8. Save response
            # ------------------------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                }
            )