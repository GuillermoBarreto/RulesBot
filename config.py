import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is not set. Add it to a .env file or your environment before running the agent."
    )
LLM_MODEL = "llama-3.3-70b-versatile"

# --- Agent ---
MAX_TOOL_ROUNDS = 5   # Maximum tool-calling loops before stopping
                      # Prevents runaway agent loops

# --- Data ---
# Resolve relative to this file so the app works no matter which
# working directory it is launched from.
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
