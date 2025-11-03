"""
Script principal: ejecuta el pipeline completo CRISP-DM.
"""

from src.datos.ingesta import cargar_datos
from src.modelos.clustering import ejecutar_clustering
from src.modelos.regresion import ejecutar_regresion
from src.agente.agente_inteligente import ejecutar_agente_inteligente

if __name__ == "__main__":
    print("\n=== INICIO PIPELINE TFM TURISTIFICACIÓN ===")
    datos = cargar_datos()
    datos_cluster = ejecutar_clustering(datos)
    ejecutar_regresion()
    ejecutar_agente_inteligente()
    print("=== PIPELINE COMPLETADO ===")
