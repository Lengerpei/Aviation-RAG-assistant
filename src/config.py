import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# ===============================
# API Keys
# ===============================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )

# ===============================
# Model Configuration
# ===============================
MODEL_NAME = "llama-3.3-70b-versatile"

# ===============================
# Embedding Model
# ===============================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===============================
# Directories
# ===============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

CHROMA_DB_DIR = os.path.join(BASE_DIR, "chromadb")

# ===============================
# Text Splitting
# ===============================
CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

# ===============================
# Retriever
# ===============================
TOP_K = 4