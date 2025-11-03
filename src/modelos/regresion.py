"""
Modelos predictivos: Random Forest y XGBoost.
Predice el impacto del turismo en precios inmobiliarios.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error
from joblib import dump

def ejecutar_regresion():
    print("\n=== Fase 3: Modelado - Regresión (Random Forest y XGBoost) ===")

    np.random.seed(42)
    datos = pd.DataFrame({
        'flujo_turistico': np.random.randint(100, 1000, 200),
        'ocupacion_hotelera': np.random.uniform(0.4, 0.95, 200),
        'oferta_inmobiliaria': np.random.randint(50, 500, 200),
        'precio_vivienda': np.random.randint(80000, 600000, 200)
    })

    X = datos[['flujo_turistico', 'ocupacion_hotelera', 'oferta_inmobiliaria']]
    y = datos['precio_vivienda']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    xgb = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    xgb.fit(X_train, y_train)

    y_pred_rf = rf.predict(X_test)
    y_pred_xgb = xgb.predict(X_test)

    r2_rf = r2_score(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
    r2_xgb = r2_score(y_test, y_pred_xgb)
    rmse_xgb = np.sqrt(mean_squared_error(y_test, y_pred_xgb))

    print(f"Random Forest → R²: {r2_rf:.3f} | RMSE: {rmse_rf:.2f}")
    print(f"XGBoost       → R²: {r2_xgb:.3f} | RMSE: {rmse_xgb:.2f}")

    dump(rf, 'reports/modelo_random_forest.joblib')
    dump(xgb, 'reports/modelo_xgboost.joblib')
    print("Modelos guardados en /reports.")
