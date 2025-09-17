from collections import deque
from typing import Deque, Dict, List

class ConversationMemory:
    def __init__(self, max_messages: int = 12):
        self_memory: Deque[dict[str, str]] = Deque (maxlen=max_messages)
        
    def add_user(self, content: str):
        self.memory.append({"role": "user", "content": content})
        
    def add_model(self, content: str):
        self.memory.append({"role": "user", "content": content})
        
    def get(self) -> List[Dict[str, str]]:
        return list(self.memory)
    
    def clear(self):
        self.memory.clear()