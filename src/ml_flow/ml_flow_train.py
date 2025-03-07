import mlflow
from mlflow.models import infer_signature
from src.data import cargar_datos
from src.ml_flow.ml_flow_model import MODELOS
from src.evaluate import calcular_metricas, guardar_matriz_confusion

def main():
    """Función principal que ejecuta el pipeline de entrenamiento y evaluación."""
    X_train, X_test, y_train, y_test = cargar_datos()
    
    mlflow.set_experiment("phishing-detections")

    for nombre_modelo, parametros, modelo in MODELOS:
        with mlflow.start_run(run_name = nombre_modelo):
            # Establecer los parametros de cada modelo
            mlflow.log_params(parametros)
            modelo.set_params(**parametros)
            
            # Entrenamiento del modelo
            modelo.fit(X_train, y_train)

            # Prediccion del modelo entrenado
            y_pred = modelo.predict(X_test)
            
            # Calcular las diferentes metricas
            accuracy, precision, f1, recall, cm = calcular_metricas(y_test, y_pred)

            # Establecer las metricas en MLflow
            mlflow.log_metrics({
                'accuracy': accuracy,
                'precision': precision,
                'f1': f1,
                'recall': recall
            })

            # Almacenar la matriz de confusion
            guardar_matriz_confusion(cm, nombre_modelo)

            # Registrar el modelo
            signature = infer_signature(X_train, modelo.predict(X_train))
            mlflow.sklearn.log_model(
                sk_model = modelo,
                artifact_path = "phising_model",
                signature = signature,
                input_example = X_train,
                registered_model_name = nombre_modelo
            )

if __name__ == "__main__":
    main()
