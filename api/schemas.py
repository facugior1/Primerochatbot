from pydantic import BaseModel


class ChatRequest(BaseModel):
    mensaje: str
    reset: bool = False
    role: str = "asistente"

class ChatResponse(BaseModel):
    respuesta: str
