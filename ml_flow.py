# Librerias
import mlflow
import psutil
from mlflow.models import infer_signature
from datasets import load_dataset
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
from tensorflow.keras.callbacks import Callback
import pandas as pd
from sklearn.metrics import confusion_matrix
from tensorflow.keras.metrics import Precision, Recall
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


# Cargar dataset
dataset = load_dataset("pirocheto/phishing-url")

# Dataset Train
df_train = pd.DataFrame(dataset['train'])
X_train = df_train.drop(columns = ['url', 'status'])
y_train = df_train['status'].values

# Dataset Test
df_test = pd.DataFrame(dataset['test'])
X_test = df_test.drop(columns = ['url', 'status'])
y_test = df_test['status'].values

# convertir a valores numericos
encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.fit_transform(y_test)

#Normalizar el dataset
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Hiperparametros
params = {
    "neuronas": 64,
    "activacion": "relu",
    "optimizador": "RMSprop",
    "batch_size": 32,
    "epochs": 10
}

#Red neuronal
def crear_modelo(neuronas=64,activacion ='relu', optimizador ='RMSprop'):
  model = Sequential()
  model.add(Dense(neuronas, activation=activacion, input_dim=X_train.shape[1]))
  model.add(Dense(neuronas, activation=activacion))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer= optimizador, metrics=['accuracy',Precision(name="precision"), Recall(name="recall")])
  return model

#callback
class MLflowCallback(Callback):
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


#iniciar mlflow
mlflow.set_experiment("phishing-detections")

with mlflow.start_run():
  
    mlflow.log_params(params)
    mlflow.log_metric("cpu_usage", psutil.cpu_percent())
    mlflow.log_metric("memory_usage", psutil.virtual_memory().percent)
    
    modelo = crear_modelo(
      neuronas=params["neuronas"],
      activacion=params["activacion"],
      optimizador=params["optimizador"]
    )
    
    history = modelo.fit(
      X_train, y_train,
      epochs=params["epochs"],
      batch_size=params["batch_size"],
      validation_data=(X_test, y_test),
      callbacks=[MLflowCallback()],      
    )    
  
        
    y_pred = modelo.predict(X_test)
    y_pred = (y_pred > 0.5).astype(int)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)
    
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No Phishing", "Phishing"], yticklabels=["No Phishing", "Phishing"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.savefig("confusion_matrix.png")
    mlflow.log_artifact("confusion_matrix.png")
    
    mlflow.set_tag("Training Info", "pishing-detection")
    signature = infer_signature(X_train, modelo.predict(X_train))
    
    model_info = mlflow.sklearn.log_model(
      sk_model=modelo,
      artifact_path="pishing-detection",
      signature=signature,
      input_example=X_train,
      registered_model_name="pishing-detection",
    )    
    
    mlflow.tensorflow.log_model(modelo, "modelo_keras")
   