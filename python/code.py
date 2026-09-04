
import socket
import platform
import getpass

def obtener_info_sistema():
    """Simula la recolección de información del sistema."""
    return {
        "usuario": getpass.getuser(),
        "sistema": platform.system(),
        "version": platform.version(),
        "arquitectura": platform.machine()
    }

def enviar_info_servidor(info):
    """Simula el envío de datos a un servidor remoto."""
    print("[SIMULACIÓN] Conectando al servidor...")
    print("[SIMULACIÓN] Enviando datos:", info)
    # Aquí NO se realiza ninguna conexión real

def main():
    print("=== Simulación de Troyano Educativo ===")
    info = obtener_info_sistema()
    enviar_info_servidor(info)
    print("[SIMULACIÓN] Finalizado.")

if __name__ == "__main__":
    main()