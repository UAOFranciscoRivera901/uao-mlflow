import mlflow
import psutil
from mlflow.models import infer_signature
from src.ml_flow.data_preprocessing import cargar_datos
from src.ml_flow.model import crear_modelo
from src.ml_flow.callbacks import MLflowCallback
from src.ml_flow.config import PARAMS
from src.ml_flow.evaluate import evaluar_modelo, guardar_matriz_confusion

def entrenar_modelo(modelo, X_train, y_train, X_test, y_test):
    """Entrena el modelo y registra métricas en MLflow."""
    modelo.fit(
        X_train, y_train,
        epochs=PARAMS["epochs"],
        batch_size=PARAMS["batch_size"],
        validation_data=(X_test, y_test),
        callbacks=[MLflowCallback()]
    )

def main():
    """Función principal que ejecuta el pipeline de entrenamiento y evaluación."""
    X_train, y_train, X_test, y_test = cargar_datos()
    
    mlflow.set_experiment("phishing-detections")
    with mlflow.start_run():
        mlflow.log_params(PARAMS)
        mlflow.log_metric("cpu_usage", psutil.cpu_percent())
        mlflow.log_metric("memory_usage", psutil.virtual_memory().percent)
        
        modelo = crear_modelo(
            neuronas=PARAMS["neuronas"],
            activacion=PARAMS["activacion"],
            optimizador=PARAMS["optimizador"],
            input_dim=X_train.shape[1]
        )
        
        entrenar_modelo(modelo, X_train, y_train, X_test, y_test)
        
        accuracy, cm = evaluar_modelo(modelo, X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)
        
        guardar_matriz_confusion(cm)
        
        signature = infer_signature(X_train, modelo.predict(X_train))
        mlflow.tensorflow.log_model(modelo, "models/modelo_keras", signature=signature)

if __name__ == "__main__":
    main()
