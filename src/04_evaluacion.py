"""
Etapa 4 - Evaluación (CRISP-DM)
Objetivo: Evaluar la precisión y coherencia de los modelos aplicados.
"""
from sklearn.metrics import r2_score, mean_absolute_error

def evaluar_modelo(modelo, X, y_real):
    y_pred = modelo.predict(X)
    r2 = r2_score(y_real, y_pred)
    mae = mean_absolute_error(y_real, y_pred)
    print(f"R²: {r2:.2f}, MAE: {mae:.2f}")
    return r2, mae
