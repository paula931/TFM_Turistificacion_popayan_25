#!/bin/bash
echo "=== INICIO PIPELINE TFM TURISTIFICACIÓN ==="
python src/01_negocio.py
python src/02_preprocesamiento.py
python src/03_modelado.py
python src/04_evaluacion.py
python src/05_agente_inteligente.py
echo "=== PIPELINE COMPLETADO ==="
