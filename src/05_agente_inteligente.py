"""
Etapa 5 - Despliegue y Agente Inteligente
Objetivo: Simular la automatización y monitoreo del fenómeno de turistificación.
"""
import random
import time

def agente_inteligente():
    niveles = ["bajo", "medio", "alto"]
    while True:
        nivel = random.choice(niveles)
        print(f"Nivel de turistificación detectado: {nivel}")
        if nivel == "alto":
            print("⚠️ Alerta: Riesgo de saturación turística. Se recomienda intervención.")
        time.sleep(2)
        break

if __name__ == "__main__":
    agente_inteligente()
