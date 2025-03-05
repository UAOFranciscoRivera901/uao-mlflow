from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import Precision, Recall

def crear_modelo(neuronas, activacion, optimizador, input_dim):
    """Crea y compila el modelo de red neuronal."""
    model = Sequential([
        Dense(neuronas, activation=activacion, input_dim=input_dim),
        Dense(neuronas, activation=activacion),
        Dense(1, activation='sigmoid')
    ])

    model.compile(
        loss='binary_crossentropy',
        optimizer=optimizador,
        metrics=['accuracy', Precision(name="precision"), Recall(name="recall")]
    )

    return model
