import os, json, difflib
import streamlit as st
from dotenv import load_dotenv

# Load .env (for API key)
load_dotenv()

try:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    _HAS_OPENAI = True
except:
    _HAS_OPENAI = False

st.set_page_config(page_title="Iron Lady FAQ Chatbot", page_icon="💬")
st.title("💬 Iron Lady – FAQ Chatbot")

# Load FAQs
KB_PATH = os.path.join(os.path.dirname(__file__), "faqs.json")
with open(KB_PATH, "r", encoding="utf-8") as f:
    KB = json.load(f)   # must be list of {"q": ..., "a": ...}

# Function: best FAQ match
def best_match(user_q: str):
    questions = [item["q"] for item in KB]
    matches = difflib.get_close_matches(user_q, questions, n=1, cutoff=0.65)
    if matches:
        q = matches[0]
        for item in KB:
            if item["q"] == q:
                return item
    return None   # no good match

# Function: AI fallback
def ai_fallback(user_q: str) -> str:
    if not _HAS_OPENAI:
        return "❌ Sorry, I don’t know the answer."
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful FAQ assistant for Iron Lady's leadership programs."},
                {"role": "user", "content": f"Answer this question: {user_q}"}
            ]
        )
        return resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ AI unavailable: {e}"

# Chat history
if "chat" not in st.session_state:
    st.session_state["chat"] = []

# Input
user_q = st.text_input("Ask a question:")
if st.button("Send") and user_q.strip():
    kb_item = best_match(user_q)
    if kb_item:  # FAQ found
        ans = kb_item["a"]
    else:        # No FAQ → AI fallback
        ans = ai_fallback(user_q)

    st.session_state["chat"].append(("You", user_q))
    st.session_state["chat"].append(("Bot", ans))

# Display chat
for role, msg in st.session_state["chat"]:
    st.write(f"**{role}:** {msg}")
