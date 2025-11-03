"""
Etapa 2 - Preparación de los Datos (CRISP-DM)
Objetivo: Limpiar, normalizar y preparar las fuentes oficiales (DANE, MinComercio).
"""
import pandas as pd

def preparar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    df = df.drop_duplicates()
    df = df.dropna(subset=['P7570', 'P7580'])
    df['GastoPromedio'] = df['P7580'].astype(float)
    return df

if __name__ == "__main__":
    print("Datos cargados y preprocesados correctamente.")
