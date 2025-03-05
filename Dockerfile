# Usar la imagen oficial de Python 3.12.2
FROM python:3.12.2-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# # Exponer el puerto de MLflow
EXPOSE 5000

# Comando para ejecutar el script principal
CMD ["python", "main_ml_flow.py"]