from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "The future of AI is amazing!"
embedding_vector = embedding_model.embed_query(text)

print(f"Embedding vector length: {len(embedding_vector)}")
print(f"Sample embedding: {embedding_vector[:5]}")
