import streamlit as st
import sys
import os

# Ensure src folder is in path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from main_pipeline import get_final_answer

# ✅ Page config
st.set_page_config(
    page_title="ML Advisor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ CLEAN + SAFE DARK UI CSS (NO BREAKING)
st.markdown("""
<style>

/* ===== REMOVE TOP WHITE HEADER ===== */
[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

/* ===== APP BACKGROUND ===== */
[data-testid="stAppViewContainer"] {
    background-color: #0B0F19;
}

/* ===== FIX BOTTOM WHITE BAR ===== */
[data-testid="stBottomBlockContainer"] {
    background-color: #111827;
    border-top: 1px solid #2A2E3E;
}

/* ===== CHAT INPUT ===== */
[data-testid="stChatInput"] textarea {
    background-color: #1C1F2E !important;
    color: white !important;
    border-radius: 10px;
}

/* Placeholder */
textarea::placeholder {
    color: #9CA3AF !important;
    font-size: 15px;
}

/* Send button */
[data-testid="stChatInput"] button {
    background-color: #4CAF50 !important;
    color: white !important;
}

/* ===== CHAT MESSAGES ===== */
[data-testid="stChatMessage"] {
    background-color: #1C1F2E;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Sidebar headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #4CAF50 !important;
}

/* ===== REMOVE EXTRA TOP SPACE ===== */
.block-container {
    padding-top: 1rem !important;
}
/* 🔥 FIX TITLE VISIBILITY */
h1, h2, h3 {
    color: #FFFFFF !important;
}

/* Subtitle */
p {
    color: #D1D5DB !important;
}
            
h1 {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px;
}

/* ===== FOOTER ===== */
.footer {
    position: fixed;
    bottom: 5px;
    width: 100%;
    text-align: center;
    color: #9CA3AF;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# ✅ SIDEBAR
with st.sidebar:

    st.markdown("## 👩‍💻 Developed By")
    st.write("Rachel Purnima J")

    st.markdown("---")

    st.markdown("## ⚙️ Model Stack")
    st.markdown("""
- LLM: OpenAI GPT  
- Embeddings: MiniLM  
- Vector DB: ChromaDB  
""")

    st.markdown("---")

    st.markdown("## 🧠 Architecture")
    st.markdown("""
- RAG  
- Web Search  
- Hybrid Retrieval  
- Intelligent Routing  
""")

# ✅ MAIN TITLE
st.title("👉 Intelligent ML Advisor (RAG + Hybrid Search System)")
st.markdown("Your intelligent assistant for Machine Learning concepts")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ✅ CHAT INPUT
query = st.chat_input("Ask anything about Machine Learning...")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_final_answer(query)
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

# ✅ FOOTER
st.markdown("""
<div class="footer">
⚡ Powered by RAG + Web Search + Intelligent Routing
</div>
""", unsafe_allow_html=True)