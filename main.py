# main.py
from src.datos.ingesta import cargar_datos
from src.modelos.clustering import ejecutar_clustering
from src.modelos.regresion import ejecutar_regresion
from src.visualizaciones.graficos import generar_graficos
from src.agente.inteligente import iniciar_agente

def main():
    print("Iniciando pipeline CRISP-DM del TFM - Turistificación en Popayán")

    datos = cargar_datos()
    ejecutar_clustering(datos)
    ejecutar_regresion(datos)
    generar_graficos(datos)
    iniciar_agente(datos)

    print(" Prototipo final ejecutado correctamente")

if __name__ == "__main__":
    main()
