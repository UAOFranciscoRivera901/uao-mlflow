import seaborn as sns
import matplotlib.pyplot as plt
import mlflow
from sklearn.metrics import accuracy_score, confusion_matrix
import os

def evaluar_modelo(modelo, X_test, y_test):
    """Evalúa el modelo y genera métricas."""
    y_pred = (modelo.predict(X_test) > 0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, cm



def guardar_matriz_confusion(cm):
    """Guarda y registra la matriz de confusión en MLflow."""
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)  # Crea la carpeta si no existe

    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["No Phishing", "Phishing"],
                yticklabels=["No Phishing", "Phishing"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    output_path = os.path.join(reports_dir, "confusion_matrix.png")
    plt.savefig(output_path)
    mlflow.log_artifact(output_path)
