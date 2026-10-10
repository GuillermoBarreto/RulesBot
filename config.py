import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# No module-level key check here: importing config (e.g. just for DATA_PATH in
# app.py) must work without an LLM key. agent._get_client() validates the key
# lazily, right before the first chat message needs it.
LLM_MODEL = "llama-3.3-70b-versatile"

# --- Agent ---
MAX_TOOL_ROUNDS = 5   # Maximum tool-calling loops before stopping
                      # Prevents runaway agent loops

# --- Data ---
# Resolve relative to this file so the app works no matter which
# working directory it is launched from.
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
