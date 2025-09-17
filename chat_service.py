from typing import Optional
from config import Settings
from roles import RolesPreset, ROLES_SYSTEM_PROMPT
from prompts import build_system_prompt, collapse_history
from memory import ConversationMemory
from llm_client import GEMINIClient

class ChattService:
    def __init__(self, roles: RolesPreset=RolesPreset.ASISTENTE):
        self.roles = roles
        self.memory = ConversationMemory(max_messages=Settings.max_history)
        self.client = GEMINIClient(
            apyi_key=Settings.api_key,
            model_name=Settings.model,)

def ask(self, prompt: str) -> str:
        system_prompt = build_system_prompt(
            ROLES_SYSTEM_PROMPT(self.roles,),
            )
        history=collapse_history(self.memory.get())
        
        response_text = self.client.generate(
            system_prompt=system_prompt,
            user_message=prompt,
            history=history,
            max_retries=Settings.max_retries,
            timeout_seconds=Settings.timeout_seconds,
        )
        