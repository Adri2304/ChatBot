from pydantic import BaseModel

class QueryRequest(BaseModel):
    pregunta: str
