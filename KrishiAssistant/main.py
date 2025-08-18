import streamlit as st
from pipeline.rag_chatbot import create_rag_chain
from pipeline.fallback import fallback_answer
from utils.translator import detect_language, translate_to_english, translate_from_english

# Initialize chatbot pipeline once
@st.cache_resource
def load_rag():
    rag, _ = create_rag_chain()
    return rag

rag = load_rag()

st.set_page_config(page_title="KrishiAssistant", page_icon="🌾", layout="wide")
st.title("🌾 Krish Advisor")
st.markdown("Your multilingual agriculture AI advisor. Ask in any language!")

# Maintain conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input box
if query := st.chat_input("Ask your agriculture-related question..."):
    # Show user message
    st.chat_message("user").write(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Detect & translate
    source_lang = detect_language(query)
    query_en = translate_to_english(query) if source_lang != "en" else query

    try:
        response = rag.invoke({"query": query_en})
        result = response.get("result", "").strip()
        sources = response.get("source_documents", [])

        if not sources or not result or "i don't know" in result.lower():
            st.info("⚠️ No strong result found. Falling back to Mistral...")
            answer_en = fallback_answer(query_en)
        else:
            answer_en = result
    except Exception:
        answer_en = fallback_answer(query_en)

    # Translate back if needed
    final_answer = (
        translate_from_english(answer_en, source_lang)
        if source_lang != "en"
        else answer_en
    )

    # Show assistant answer
    with st.chat_message("assistant"):
        st.write(final_answer)

    st.session_state.messages.append({"role": "assistant", "content": final_answer})
