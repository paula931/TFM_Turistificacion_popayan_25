"""
Carga y preprocesamiento inicial de datos.
Simula la lectura de microdatos de turismo (DANE, MinComercio).
"""

import pandas as pd
import numpy as np

def cargar_datos():
    print("\n=== Fase 1: Comprensión y Carga de Datos ===")
    np.random.seed(42)

    datos = pd.DataFrame({
        'flujo_turistico': np.random.randint(100, 1000, 200),
        'ocupacion_hotelera': np.random.uniform(0.4, 0.95, 200),
        'oferta_inmobiliaria': np.random.randint(50, 500, 200),
        'precio_vivienda': np.random.randint(80000, 600000, 200)
    })
    
    print(f"Datos cargados: {datos.shape[0]} registros.")
    return datos
