# DevDesk AI Support Engineer

## 📌 Project Overview

This project is an **AI-powered technical support system** that uses **Retrieval-Augmented Generation (RAG)** to answer developer support questions using relevant technical documentation.

The goal is **not simply to connect an LLM to a chatbot**, but to demonstrate how an AI support system can combine **semantic search, vector retrieval, reranking, grounded generation, and intelligent escalation** to provide more reliable technical support.

The system uses **public GitHub REST API documentation** together with **fictional DevDesk internal support documentation** as its knowledge base.

## 🧠 Problem Statement

Technical support systems often need to answer questions using large amounts of documentation.

A direct LLM-based chatbot can generate responses that are:

- Not grounded in the actual documentation
- Inaccurate or unsupported
- Missing important troubleshooting information
- Unsafe for critical issues such as security incidents or data loss

This project addresses these problems by retrieving relevant documentation before generating an answer and by automatically identifying issues that should be escalated to human support.

## 📚 Knowledge Base

The system uses two types of documentation.

### Public Technical Documentation

The knowledge base includes selected **GitHub REST API documentation**, covering topics such as:

- REST API fundamentals
- Authentication
- Rate limits
- Troubleshooting
- API best practices
- Repositories
- Repository contents
- REST API quickstart

### DevDesk Internal Documentation

The project also includes fictional DevDesk documentation covering:

- Company overview
- Support policies
- Escalation policies
- Frequently asked questions

This combination simulates how an enterprise AI support system can use both **external technical documentation and internal company knowledge**.

## ⚙️ System Architecture

```text
                    User Question
                         ↓
                Semantic Escalation
                         ↓
              ┌──────────┴──────────┐
              │                     │
        Critical Issue        Normal Issue
              │                     ↓
              │              FAISS Retrieval
              │                     ↓
              │             Cross-Encoder
              │                Reranking
              │                     ↓
              │              Context Building
              │                     ↓
              │                Gemini LLM
              │                     ↓
              │              Answer + Sources
              │
              ↓
        Human Support
````

## 🔎 Retrieval-Augmented Generation (RAG)

The system follows a multi-stage RAG pipeline.

### 1️⃣ Document Loading

Markdown documents are loaded from the project knowledge base.

### 2️⃣ Document Chunking

Large documents are divided into smaller chunks so that relevant sections can be retrieved efficiently.

### 3️⃣ Semantic Embeddings

**Sentence Transformers** are used to convert document chunks and user questions into numerical vector representations.

This allows the system to search based on **semantic meaning rather than exact keyword matching**.

### 4️⃣ Vector Retrieval

The embeddings are stored in a **FAISS vector index**.

When a user asks a question, FAISS retrieves the most semantically similar document chunks.

### 5️⃣ Cross-Encoder Reranking

The retrieved documents are passed through a **Cross-Encoder reranker** to improve the ordering of the most relevant results.

This provides a second relevance-checking stage after vector retrieval.

### 6️⃣ Context Building

The highest-ranked document chunks are combined into a context that is provided to the language model.

### 7️⃣ Gemini Response Generation

**Gemini** generates the final response using the retrieved documentation as context.

The model is instructed to:

* Use the provided documentation
* Avoid inventing information
* Avoid inventing API endpoints or features
* Clearly state when documentation is insufficient
* Provide practical troubleshooting guidance when supported

## 🚨 Semantic Escalation

One of the main features of the project is **semantic escalation**.

Instead of relying only on keyword-based rules, the system uses **Sentence Transformer embeddings and cosine similarity** to determine whether a customer issue is semantically similar to predefined critical support scenarios.

Examples include:

* Security vulnerabilities
* Unauthorized account access
* Compromised accounts
* Data loss
* Missing customer data
* Data corruption
* Platform-wide outages
* Multiple unavailable services

For example:

```text
"My account has been hacked."
```

can be recognized as a security-related issue even without depending on an exact keyword rule.

When escalation is triggered, the system recommends **human support instead of generating a normal AI response**.

## 🤖 LLM Response Generation

The project uses the **Gemini API** for response generation.

The LLM receives:

```text
Customer Question
        +
Retrieved Documentation
        ↓
     Gemini
        ↓
Grounded Technical Response
```

The system is designed to reduce unsupported responses by restricting the model to the retrieved knowledge base context.

## 📖 Source Attribution

The chatbot **shows the source documentation used for each generated response**.

After an answer is generated, the user can open the **"View Sources"** section to see the documentation files retrieved by the RAG pipeline.

This makes the response more:

* Transparent
* Traceable
* Explainable

Users can therefore understand **where the technical information came from**, rather than receiving an answer without any indication of its supporting documentation.

## 💻 Streamlit Interface

The project includes an interactive **Streamlit-based chatbot interface**.

The interface provides:

* Conversational chat experience
* Technical issue input
* AI-generated technical support responses
* Human support escalation messages
* **Source attribution through the "View Sources" section**
* **Light and dark mode support through Streamlit's theme**
* Responsive and clean chatbot interface
* **Screen recording support**, allowing the application workflow and chatbot interactions to be easily demonstrated and documented

The interface is designed to work with both **light and dark themes** without forcing a single application-wide color scheme.

## 🛠️ Tech Stack

* **Python**
* **Sentence Transformers**
* **FAISS**
* **Cross-Encoder**
* **scikit-learn**
* **RAG**
* **Gemini API**
* **Streamlit**

## 📁 Project Structure

```text
ai-support-engineer/
│
├── app/
│   └── chatbot.py
│
├── scripts/
│   ├── data/
│   │   ├── github_docs/
│   │   └── internal_docs/
│   │
│   └── download_github_docs.py
│
├── src/
│   ├── rag/
│   │   ├── document_loader.py
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── reranker.py
│   │   ├── context_builder.py
│   │   ├── semantic_escalation.py
│   │   └── rag_pipeline.py
│   │
│   └── llm/
│       └── llm_client.py
│
├── tests/
│   ├── test_llm.py
│   └── test_rag.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shraddhagupta2103/devdesk-ai-support-engineer.git
cd devdesk-ai-support-engineer
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Do **not** commit the `.env` file to GitHub.

### 5️⃣ Download the Documentation

Run:

```bash
python scripts/download_github_docs.py
```

This downloads the selected GitHub documentation into:

```text
scripts/data/github_docs/
```

The DevDesk internal documentation is also stored under:

```text
scripts/data/internal_docs/
```

### 6️⃣ Build the Vector Store

Run the project's vector-store creation process to generate the FAISS index and stored document chunks.

### 7️⃣ Start the Chatbot

```bash
streamlit run app/chatbot.py
```

The application will open in the browser.

## 💬 Example Questions

### Technical Support

```text
Why am I getting a 401 error?
```

```text
Why am I getting a 403 error?
```

```text
Why am I getting a 429 error?
```

```text
How does API authentication work?
```

### Escalation Scenarios

```text
My account has been hacked.
```

```text
My customer data has disappeared.
```

```text
Multiple services are unavailable.
```

These types of questions can trigger semantic escalation to human support.

## 💼 What This Project Demonstrates

✔ Retrieval-Augmented Generation (RAG)

✔ Semantic document retrieval

✔ FAISS vector search

✔ Cross-Encoder reranking

✔ Semantic similarity-based escalation

✔ LLM-powered technical support

✔ Documentation-grounded responses

✔ Source attribution

✔ Human-in-the-loop support workflow

✔ Streamlit chatbot development

✔ Light and dark theme support

✔ Production-oriented AI system design

## 📌 Future Improvements

* Add automated RAG evaluation metrics
* Add retrieval and answer quality benchmarking
* Add confidence-based fallback handling
* Add conversation analytics
* Add document upload and automatic indexing
* Add authentication and role-based access
* Add monitoring for retrieval and response quality
* Deploy the application as a production service

## 🏁 Final Note

This project focuses on **building a practical AI support engineering system rather than simply creating an LLM chatbot**.

It demonstrates how modern AI applications can combine **semantic search, vector databases, reranking, RAG, LLMs, and intelligent escalation** to create a more reliable and production-oriented support workflow.

**Author:** Shraddha Gupta


