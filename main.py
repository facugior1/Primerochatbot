import sys
from roles import RolesPreset
from config import Settings
from chat_service import ChattService

def chose_roles() -> RolesPreset:
    print("Elegi un rol")
    print("1. Profesor, 2. Traductor, 3. Programador, 4. Asistente",)
    
    sel = input("Selecciona una opcion (1-4): ")
    
    mappding = {
        "1": RolesPreset.PROFESOR,
        "2": RolesPreset.TRADUCTOR,
        "3": RolesPreset.PROGRAMADOR,
        "4": RolesPreset.ASISTENTE,
    } 
    return mappding.get(sel, RolesPreset.ASISTENTE) #siempre por defecto es asistente

def print_help():
    print("\nComandos disponibles:")
    print(":rol profesor|traductor|programador|asistente - Cambia el rol actual")
    print(":reset - Reinicia la conversación")
    print(":exit - Salir de la aplicación")
    
def main():
    print("{Settings.system_name}")
    role = chose_roles()
    chat = ChattService(roles = role)
    print_help()

    while True:
        try:
            user_input = input("\nVos: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...🦖🦖 ")
            break
        if not user_input:
            continue

        if user_input.lower() == ":exit" or user_input.lower() == "salir":
            print("Saliendo...🦖🦖 ")
            break
        if user_input.lower() == ":reset" or user_input.lower() == "reset":
            print("Conversacion reiniciada.")
            chat.reset()
            continue
        if user_input.lower().startswith(":rol"):
            new_role_str = user_input[5:].strip().upper()
            mapping = {
                "PROFESOR": RolesPreset.PROFESOR,
                "TRADUCTOR": RolesPreset.TRADUCTOR,
                "PROGRAMADOR": RolesPreset.PROGRAMADOR,
                "ASISTENTE": RolesPreset.ASISTENTE,
            }
            if new_role_str in mapping:
                chat.set_role(mapping[new_role_str])
                print(f"Rol cambiado a {new_role_str}.")
            else:
                print("Rol no reconocido. Usa profesor, traductor, programador o asistente.")
            continue
        if user_input.lower() == ":ayuda" or user_input.lower() == "ayuda":
            print_help()
            continue
        try:
            answer = chat.ask(user_input)
            print(f"\nBot: {answer}")
        except Exception as e:
            print(f"Error al obtener respuesta: {e}")

if __name__ == "__main__":
    main()