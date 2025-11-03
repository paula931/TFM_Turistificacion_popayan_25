"""
Etapa 3 - Modelado (CRISP-DM)
Objetivo: Aplicar modelos de clustering y predicción (K-Means, DBSCAN, Random Forest, XGBoost).
"""
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def clustering_kmeans(df):
    X = df[['GastoPromedio']]
    modelo = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = modelo.fit_predict(X)
    print("Clustering completado. Etiquetas asignadas.")
    return df

def modelo_random_forest(df):
    X = df[['P7579']]
    y = df['P7580']
    modelo = RandomForestRegressor(random_state=42)
    modelo.fit(X, y)
    print("Modelo Random Forest entrenado correctamente.")
    return modelo

if __name__ == "__main__":
    print("Modelado ejecutado correctamente.")
