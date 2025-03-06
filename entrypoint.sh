#!/bin/bash
# Start MLflow UI in the foreground
mlflow ui --host 0.0.0.0 --port 5000 &

# Run both Python scripts in the background
python main_ml_flow.py &
python main_comet.py &

# Esperar a que todos los procesos en segundo plano terminen
wait
