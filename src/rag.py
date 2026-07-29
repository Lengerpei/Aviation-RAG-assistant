from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from config import (
    CHROMA_DB_DIR,
    EMBEDDING_MODEL,
    MODEL_NAME,
    GROQ_API_KEY,
    TOP_K,
)

# ============================
# Embeddings
# ============================

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

# ============================
# Load Chroma Database
# ============================

vector_db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": TOP_K}
)

# ============================
# Groq LLM
# ============================

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=0
)

# ============================
# Prompt
# ============================

prompt = ChatPromptTemplate.from_template(
"""
You are AviationGPT.

Use ONLY the context below to answer the user's question.

If the answer is not contained in the context, say:

"I don't have enough information in my aviation knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""
)

# ============================
# Helper
# ============================

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# ============================
# LCEL Chain
# ============================

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)


def ask_question(question: str):
    return rag_chain.invoke(question)