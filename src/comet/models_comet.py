from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import Precision, Recall
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from src.comet.config_comet import PARAMS

def crear_modelo(neuronas=64,activacion ='relu', optimizador ='RMSprop',input_dim=None):
  model = Sequential()
  model.add(Dense(neuronas, activation=activacion, input_dim=input_dim))
  model.add(Dense(neuronas, activation=activacion))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer= optimizador, metrics=['accuracy',Precision(name="precision"), Recall(name="recall")])
  return model

def obtener_modelos(input_dim):
    return {
        "LOGISTIC_REGRESSION": LogisticRegression(max_iter=1, warm_start=True),
        "RANDOM_FOREST": RandomForestClassifier(n_estimators=1, max_depth=PARAMS["max_depth"], warm_start=True),
        "RED_NEURONAL": crear_modelo(input_dim)
    }
