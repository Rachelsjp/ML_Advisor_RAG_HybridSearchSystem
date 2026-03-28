# 👉 Intelligent ML Advisor (RAG + Hybrid Search System)

An intelligent Machine Learning assistant that combines **Retrieval-Augmented Generation (RAG)**, **Hybrid Retrieval**, and **Real-time Web Search** to deliver accurate, context-aware answers.

---

## 🔥 Project Overview

This project demonstrates how to build a **production-style GenAI system** that:

- 📚 Uses **RAG (Vector Database)** for domain-specific knowledge retrieval
- 🔀 Implements **Hybrid Retrieval (RAG + Web)** for partially answered queries
- 🌐 Falls back to **Web Search** when internal knowledge is insufficient
- 🧠 Uses **Intelligent Routing** to dynamically choose the best strategy
- 📄 Provides **Source Attribution** for transparency and trust

---

## 🧠 Key Features

- 📚 **RAG-based Knowledge Retrieval**
- 🔀 **Hybrid Retrieval (RAG + Web)**
- 🌐 **Web Search Fallback (SerpAPI)**
- 🧠 **Intelligent Routing Logic**
- 📄 **Source Attribution**
- 💬 **Chat-based UI (Streamlit)**
- 🎨 **Custom Dark Theme UI**

---

## 🏗️ Architecture

User Query
│
▼
RAG Pipeline (Vector DB Search)
│
▼
Similarity Score + Answer
│
▼
Routing Logic (Router.py)
│
├──▶ RAG Only
│
├──▶ Hybrid (RAG + Web)
│
└──▶ Web Only
│
▼
Final Answer Returned to UI (Streamlit)


---

## ⚙️ Tech Stack

- **LLM**: OpenAI GPT
- **Embeddings**: Sentence Transformers (MiniLM)
- **Vector DB**: ChromaDB
- **Framework**: LangChain
- **Frontend**: Streamlit
- **Web Search**: SerpAPI

---

## 🔄 Workflow

1. User asks a question
2. System retrieves relevant documents using RAG
3. Computes similarity score
4. Router decides:

   - ✅ RAG → if strong match
   - 🔀 Hybrid → if partial match
   - 🌐 Web → if weak/no match

5. Final response generated and displayed

---

🎯 Routing Logic (Core Decision Engine)
if score < 0.8:
    return "rag"
elif 0.8 <= score < 1.5:
    return "hybrid"
else:
    return "web"
🔁 Fallback & Hybrid Strategy
Scenario	Behavior
Strong knowledge match	📚 RAG only
Partial knowledge	🔀 Hybrid (RAG + Web)
No relevant data	🌐 Web fallback
⚠️ Important Insight

Hybrid retrieval is intentionally rare.

Triggered only when internal knowledge is partially useful
Avoids mixing weak + noisy responses
Ensures cleaner and more reliable outputs
🧠 Key Learnings
🔥 1. RAG is NOT just retrieval
LLM enhances retrieved content
Generates structured and readable answers
🔥 2. Data formatting is critical
Poor structure → poor retrieval
Clean documents → accurate answers
🔥 3. Routing is the brain of the system
Prevents hallucination
Improves answer reliability
🔥 4. Hybrid behavior insight
Does NOT always trigger
Happens only when:
RAG is useful BUT incomplete
🔥 5. LLM reasoning vs Real knowledge
Type	Source
📚 RAG Answer	Internal documents
🌐 Web Answer	Real-time search
🧠 LLM Reasoning	Generated explanation
🖼️ Screenshots
💬 Chat UI

📂 Project Structure
ML_ADVISOR/
│
├── data/
├── chroma_db/
├── screenshots/
│   └── chat.png
│
├── src/
│   ├── ingest_docs.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── router.py
│   ├── web_search.py
│   ├── main_pipeline.py
│   ├── streamlit_app.py
│
├── .env
├── requirements.txt
└── README.md
🚀 How to Run
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Setup environment variables

Create .env file:

OPENAI_API_KEY=your_key
SERPAPI_API_KEY=your_key
3️⃣ Ingest documents
python src/ingest_docs.py
4️⃣ Run the app
streamlit run src/streamlit_app.py
💼 Use Cases
ML Concept Assistant
Interview Preparation Tool
Learning Companion
Domain-specific Q&A system
⚡ Future Improvements
RAG evaluation (RAGAS)
Feedback loop
Better hybrid tuning
Multi-agent system
👩‍💻 Developed By

Rachel Purnima J

📌 Note

This project was built as part of hands-on learning in Generative AI systems, focusing on:

RAG architecture
Hybrid retrieval
LLM reasoning
Intelligent routing
🌟 Final Thought

Building GenAI systems is not just about using LLMs —
it's about combining data, retrieval, reasoning, and decision-making effectively
