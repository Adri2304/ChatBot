from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer('all-MiniLM-L6-v2')

def obtener_embedding(texto: str) -> list:
    return modelo.encode([texto])[0].tolist()
