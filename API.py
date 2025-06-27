from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas.query import QueryRequest
from models.embedding_model import obtener_embedding
from services.chroma_service import obtener_contexto
from services.ollama_service import preguntar_a_gemma2b

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/query")
async def responder_pregunta(data: QueryRequest):
    pregunta = data.pregunta.strip()

    try:
        # Generar el embedding de la pregunta
        embedding = obtener_embedding(pregunta)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generando embeddings: {e}")

    try:
        # Buscar los embeddings parecidos en la BD para optener el contexto
        contexto = obtener_contexto(embedding)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error consultando base vectorial: {e}")

    prompt = f"""Contesta detalladamente la siguiente pregunta basándote en el contexto proporcionado. Si no sabes la respuesta, indica que no estás seguro.

Contexto:
{contexto}

Pregunta: {pregunta}
Respuesta:"""

    try:
        #Le paso el prompt al LLM
        respuesta = preguntar_a_gemma2b(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar respuesta: {e}")

    return {"respuesta": respuesta}
