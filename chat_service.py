from typing import Optional
from config import Settings
from roles import RolesPreset, ROLES_SYSTEM_PROMPT
from prompts import build_system_prompt, collapse_history
from memory import ConversationMemory
from llm_client import GeminiClient

class ChattService:
    def __init__(self, roles: RolesPreset=RolesPreset.ASISTENTE):
        self.roles = roles
        self.memory = ConversationMemory(max_messages=Settings.max_history)
        self.client = GeminiClient(
            api_key=Settings.api_key,
            model_name=Settings.model,)
#esta funcion le hace una pregunta al modelo y guarda el contexto
def ask(self, prompt: str) -> str:
        system_prompt = build_system_prompt(
            ROLES_SYSTEM_PROMPT(self.roles,),
            )
        #obtener el historial de la conversacion
        history=collapse_history(self.memory.get())
        #llamar a gemini para obtener la respuesta
        response_text = self.client.generate(
            system_prompt=system_prompt,
            user_message=prompt,
            history=history,
            max_retries=Settings.max_retries,
            timeout_seconds=Settings.timeout_seconds,
        )
        #actializar la memoria con la nueva interaccion
        self.memory.add_user_message(prompt)
        self.memory.add_model(response_text)
        return response_text
def reset_memory(self):
        self.memory.clear()