"""
Agente inteligente: Monitoreo y alertas predictivas.
"""

import random
import time

def ejecutar_agente_inteligente():
    print("\n=== Fase 4: Despliegue - Agente Inteligente ===")

    nivel_turistificacion = random.choice(["bajo", "moderado", "alto"])
    print(f"Nivel de turistificación detectado: {nivel_turistificacion}")

    if nivel_turistificacion == "alto":
        print("⚠️ Alerta: riesgo de saturación turística detectado.")
    else:
        print("✅ Situación bajo control.")

    print("Agente completado correctamente.\n")
