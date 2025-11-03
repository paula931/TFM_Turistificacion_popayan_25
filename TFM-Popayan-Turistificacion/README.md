# TFM – Turistificación en Popayán (Prototipo reproducible por consola)

Este repo contiene el **prototipo funcional** para el TFM, organizado según **CRISP-DM**:

1. **Comprensión del negocio** → `docs/01_negocio.md`
2. **Comprensión de los datos** → `src/ingesta.py` (lee microdatos EIGT DANE/MinComercio)
3. **Preparación de datos** → `src/limpieza_preparacion.py` (limpieza, normalización, diccionarios)
4. **Ingeniería de características** → `src/features_geo.py` (agregaciones y coordenadas aproximadas), `src/nlp_sentimientos.py`
5. **Modelado** → `src/modelado_clustering.py` (K-Means/DBSCAN), `src/modelado_regresion.py` (RF/XGB)
6. **Evaluación** → `src/evaluacion_reportes.py` (métricas, gráficos, tablas), `reports/figures/`
7. **Despliegue (prototipo)** → `src/agente_inteligente.py` (simulación: monitoreo, alertas, recomendaciones)

**Pipeline (local):**
```bash
bash run_all.sh
# Crear entorno virtual
python -m venv .venv
source .venv/Scripts/activate  # En Windows
# Instalar librerías
pip install pandas numpy scikit-learn geopandas matplotlib seaborn nltk xgboost
pip freeze > requirements.txt

# Crear carpetas (si faltan)
mkdir -p src data/raw data/processed reports/figures notebooks
# Crear entorno virtual
python -m venv .venv
source .venv/Scripts/activate  # En Windows
# Instalar librerías
pip install pandas numpy scikit-learn geopandas matplotlib seaborn nltk xgboost
pip freeze > requirements.txt

# Crear carpetas (si faltan)
mkdir -p src data/raw data/processed reports/figures notebooks
cat > src/01_negocio.py <<'EOF'
"""
Fase 1: Entendimiento del negocio
Objetivo: comprender el fenómeno de la turistificación y definir variables clave.
"""
def resumen_objetivos():
    objetivos = [
        "Analizar el impacto de la turistificación en Popayán",
        "Identificar patrones de comportamiento turístico",
        "Proponer estrategias sostenibles basadas en datos"
    ]
    print("��� Objetivos del proyecto:")
    for obj in objetivos:
        print("-", obj)

if __name__ == "__main__":
    resumen_objetivos()
