import os
from dotenv import load_dotenv
import google.generativeai as genai

#APi key

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.api_key = API_KEY

#confi. model gemini
genai.configure(api_key=API_KEY)
modelo = genai.GenerativeModel("gemini-1.5-flash")

chat = modelo.start_chat()
