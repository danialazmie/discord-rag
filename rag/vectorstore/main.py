import os

from langchain_pinecone import PineconeVectorStore
from src.credentials import PINECONE_API_KEY, OPENAI_API_KEY
from langchain_openai import OpenAIEmbeddings

INDEX_NAME = 'ragv2'
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

embedding = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY
)

vectorstore = PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embedding
)