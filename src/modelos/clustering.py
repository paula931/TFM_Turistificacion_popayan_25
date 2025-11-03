"""
Módulo: clustering.py
Realiza agrupamiento de zonas turísticas con K-Means y DBSCAN.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler

def ejecutar_clustering(datos):
    print("\n=== Fase 2: Modelado - Clustering (K-Means y DBSCAN) ===")

    X = datos[['flujo_turistico', 'ocupacion_hotelera', 'oferta_inmobiliaria']]
    X_scaled = StandardScaler().fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42)
    datos['cluster_kmeans'] = kmeans.fit_predict(X_scaled)

    dbscan = DBSCAN(eps=0.6, min_samples=5)
    datos['cluster_dbscan'] = dbscan.fit_predict(X_scaled)

    print("Clusters generados correctamente (K-Means y DBSCAN).")
    return datos
