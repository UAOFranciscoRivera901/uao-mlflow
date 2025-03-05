import comet_ml
import tensorflow as tf
from tensorflow.keras.callbacks import Callback
from comet_logger import iniciar_experimento
from data import cargar_datos
from model import crear_modelo
from config import PARAMS
from sklearn.metrics import confusion_matrix

class CometCallback(Callback):
    def __init__(self, experiment):
        self.experiment = experiment

    def on_epoch_end(self, epoch, logs=None):
        self.experiment.log_metric("train_loss", logs["loss"], step=epoch)
        self.experiment.log_metric("val_loss", logs["val_loss"], step=epoch)
        self.experiment.log_metric("train_accuracy", logs["accuracy"], step=epoch)
        self.experiment.log_metric("val_accuracy", logs["val_accuracy"], step=epoch)
        self.experiment.log_metric("train_precision", logs["precision"], step=epoch)
        self.experiment.log_metric("val_precision", logs["val_precision"], step=epoch)
        self.experiment.log_metric("train_recall", logs["recall"], step=epoch)
        self.experiment.log_metric("val_recall", logs["val_recall"], step=epoch)

def entrenar_modelo():
    experiment = iniciar_experimento()
    X_train, X_test, y_train, y_test = cargar_datos()
    epochs = PARAMS.pop("epochs", 10)
    batch_size = PARAMS.pop("batch_size", 10)
    
    modelo = crear_modelo(input_dim=X_train.shape[1], **PARAMS)

    comet_callback = CometCallback(experiment)
    
    history = modelo.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_test, y_test),
        callbacks=[comet_callback]
    )

    y_pred = modelo.predict(X_test)
    y_pred = (y_pred > 0.5).astype(int)

    matrix = confusion_matrix(y_test, y_pred)
    labels = ["legitimate", "phishing"]
    experiment.log_confusion_matrix(matrix=matrix, labels=labels)

    experiment.end()

if __name__ == "__main__":
    entrenar_modelo()