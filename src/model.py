from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import Precision, Recall

"""Pull de modelos con sus respectivos parámetros que se van a evaluar en MLflow."""
MODELOS = [
    (
        "Regresion_Logistica",
        {"solver": "lbfgs", "max_iter": 100},
        LogisticRegression()
    ),
    (
        "Arbol_Decision",
        {"max_depth": 5},
        DecisionTreeClassifier()
    ),
    (
        "Bosque_Aleatorio",
        {"n_estimators": 30},
        RandomForestClassifier()
    )
]

def crear_modelo(neuronas=64, activacion='relu', optimizador='RMSprop', input_dim=None):
    model = Sequential([
        Dense(neuronas, activation=activacion, input_dim=input_dim),
        Dense(neuronas, activation=activacion),
        Dense(1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy', optimizer=optimizador,
                  metrics=['accuracy', Precision(name="precision"), Recall(name="recall")])
    
    return model