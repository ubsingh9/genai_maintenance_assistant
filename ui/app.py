# streamlit_app.py

import streamlit as st
import sys
import os
# Add root folder to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.query import get_qa_chain

qa_chain = get_qa_chain()

# Page config
# ✅ Set page config BEFORE anything else
st.set_page_config(
    page_title="Retail SKU Demand Assistant",
    page_icon="🛍️",
    layout="wide"
)

st.title("Gen AI Maintenance Assistant")
st.markdown("""
Ask any question from the this dump truck manual. The Gen AI assistant will retrieve context and answer accurately
""")


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display previous chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"👤 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Assistant:** {msg}")

# Input field at bottom
query = st.chat_input("Ask a question...")

if query:
    st.session_state.messages.append(("user", query))
    with st.spinner("Thinking..."):
        response = qa_chain.run(query)
    st.session_state.messages.append(("ai", response))
    st.rerun()