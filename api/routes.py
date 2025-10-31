from fastapi import APIRouter, HTTPException
from api.schemas import ChatRequest, ChatResponse
from chat_service import ChattService
from roles import RolesPreset


router = APIRouter()

chat_service = ChattService(roles=RolesPreset.ASISTENTE)

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.mensaje:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")

    if request.reset:
        chat_service.reset()
        # Si se proporciona rol, intentar cambiarlo (verificar existencia primero)
        if request.role:
            rol_lower = request.role.strip().lower()
            try:
                new_role = RolesPreset[rol_lower.upper()]  # asume nombres de enum en mayúsculas
                chat_service.set_role(new_role)
            except KeyError:
                raise HTTPException(status_code=400, detail=f"Rol no válido: {request.role}")
        return ChatResponse(respuesta="Conversación reiniciada.")

    try:
        respuesta = chat_service.ask(request.mensaje)
        return ChatResponse(respuesta=respuesta)
    except Exception as e:1
    raise HTTPException(status_code=500, detail=str(e)) 