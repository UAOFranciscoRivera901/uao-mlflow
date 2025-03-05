import mlflow
import psutil
from tensorflow.keras.callbacks import Callback

class MLflowCallback(Callback):
    """Callback para registrar métricas en MLflow después de cada época."""
    def on_epoch_end(self, epoch, logs=None):
        if logs is not None:
            mlflow.log_metric("train_loss", logs["loss"], step=epoch)
            mlflow.log_metric("val_loss", logs["val_loss"], step=epoch)
            mlflow.log_metric("train_accuracy", logs["accuracy"], step=epoch)
            mlflow.log_metric("val_accuracy", logs["val_accuracy"], step=epoch)
            mlflow.log_metric("train_precision", logs["precision"], step=epoch)
            mlflow.log_metric("val_precision", logs["val_precision"], step=epoch)
            mlflow.log_metric("train_recall", logs["recall"], step=epoch)
            mlflow.log_metric("val_recall", logs["val_recall"], step=epoch)
