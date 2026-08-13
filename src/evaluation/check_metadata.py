from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import (
    CHROMA_DB_DIR,
    EMBEDDING_MODEL,
)


embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

vector_db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings,
)


data = vector_db.get(
    limit=5,
    include=["documents", "metadatas"]
)


print("\nCHROMA METADATA")
print("=" * 60)

for metadata in data["metadatas"]:

    print(metadata)