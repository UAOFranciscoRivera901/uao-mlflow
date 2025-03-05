# Librerias
import comet_ml
from comet_ml import Experiment
from datasets import load_dataset
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
from tensorflow.keras.callbacks import Callback
import pandas as pd
from sklearn.metrics import confusion_matrix
from tensorflow.keras.metrics import Precision, Recall


#Unirse a comet_ml
experiment = comet_ml.Experiment(
    api_key="zf9t8KH3vUJq9o3PraFgGtfOX",
    project_name="phishing-detection",
    workspace="anfeco20"
)

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

#Red neuronal
def crear_modelo(neuronas=64,activacion ='relu', optimizador ='RMSprop'):
  model = Sequential()
  model.add(Dense(neuronas, activation=activacion, input_dim=X_train.shape[1]))
  model.add(Dense(neuronas, activation=activacion))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer= optimizador, metrics=['accuracy',Precision(name="precision"), Recall(name="recall")])
  return model

modelo=crear_modelo()
modelo.summary()

#Callback de epocas
class CometCallback(Callback):
    def on_epoch_end(self, epoch, logs=None):
        experiment.log_metric("train_precision", logs["precision"], step=epoch)
        experiment.log_metric("val_precision", logs["val_precision"], step=epoch)
        experiment.log_metric("train_recall", logs["recall"], step=epoch)
        experiment.log_metric("val_recall", logs["val_recall"], step=epoch)              
# enviar datos a comet ml
comet_callback = CometCallback()

history = modelo.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_data=(X_test, y_test),
    callbacks=[comet_callback]) # integrar con comet ml

y_pred = modelo.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)
matrix = confusion_matrix(y_true=y_test, y_pred=y_pred)
matrix = confusion_matrix(y_test, y_pred)
labels = ["legitimate", "pishing"]
experiment.log_confusion_matrix(matrix=matrix, labels=labels)

experiment.end() # terminar el experimento