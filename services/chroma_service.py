import chromadb
# from chromadb.config import Settings

chroma_client = chromadb.PersistentClient(path="./chroma_ets")
coleccion = chroma_client.get_or_create_collection("ets_docs")

def obtener_contexto(embedding: list) -> str:
    resultados = coleccion.query(
        query_embeddings=[embedding],
        n_results=3
    )
    docs = resultados['documents'][0]
    return "\n---\n".join(docs)
