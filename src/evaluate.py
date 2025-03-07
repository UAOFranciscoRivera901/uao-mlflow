import comet_ml
import seaborn as sns
import matplotlib.pyplot as plt
import mlflow
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, confusion_matrix
import os

def calcular_metricas(y_test, y_pred):
    """
    Calculo de métricas y generació de la matriz de confusión.

    Args:
        y_test: valores reales.
        y_pred: valores predichos predichos por el modelo.

    Returns:
        Metricas accuracy, precision, f1_score, recall y la matriz de confusión.
    """
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, precision, f1, recall, cm

def evaluar_modelo(modelo, X_test, y_test):
    """Evalúa el modelo y genera métricas."""
    y_pred = (modelo.predict(X_test) > 0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, cm

def guardar_matriz_confusion(cm, nombre_modelo):
    """
    Guarda y registra la matriz de confusión en MLflow.

    Args:
        cm: matriz de confusión.
        nombre_modelo: nombre del modelo que genera la matriz de confusión.

    Returns:
        Matriz de confusión guardad en formato .png
    """
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)  # Crea la carpeta si no existe

    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["No Phishing", "Phishing"],
                yticklabels=["No Phishing", "Phishing"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    output_path = os.path.join(reports_dir, f"confusion_matrix_{nombre_modelo}.png")
    plt.savefig(output_path)
    mlflow.log_artifact(output_path)