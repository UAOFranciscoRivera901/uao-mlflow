# Usar la imagen oficial de Python 3.12.2
FROM python:3.12.2-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1
# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . /app/


RUN chmod +x /app/entrypoint.sh
# # Exponer el puerto de MLflow
EXPOSE 5000
# Set up MLflow tracking server
ENV MLFLOW_TRACKING_URI=/app/mlruns

# Comando para ejecutar el script principal
#CMD ["python", "main_ml_flow.py"]
#CMD ["/app/entrypoint.sh"]