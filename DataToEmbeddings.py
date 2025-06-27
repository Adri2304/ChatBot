import os
import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.config import Settings

CARPETA_TXT = "./Data"

# Inicializar modelo de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Inicializar la base vectorial con Chroma
chroma_client = chromadb.PersistentClient(path="./chroma_ets")

coleccion = chroma_client.get_or_create_collection("ets_docs")

for archivo in os.listdir(CARPETA_TXT):
    if archivo.endswith(".txt"):
        with open(os.path.join(CARPETA_TXT, archivo), "r", encoding="utf-8") as f:
            texto = f.read()

        # Opcional: dividir en fragmentos si es muy largo
        fragmentos = [texto[i:i+1000] for i in range(0, len(texto), 1000)]

        embeddings = modelo.encode(fragmentos).tolist()

        for i, fragmento in enumerate(fragmentos):
            coleccion.add(
                documents=[fragmento],
                embeddings=[embeddings[i]],
                ids=[f"{archivo}_{i}"]
            )

print("Se crearon y se guardaron los Enbeddings correctamente")
