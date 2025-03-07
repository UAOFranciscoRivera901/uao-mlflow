from src.comet.models_comet import crear_modelo
from src.comet.config_comet import PARAMS
from tensorflow.keras.models import Sequential

def test_crear_modelo():
    # Obtener el modelo que se va a probar
    modelo = crear_modelo(neuronas = PARAMS["neuronas"],
                          activacion = PARAMS["activacion"],
                          optimizador = PARAMS["optimizador"])

    # Verificar que el modelo sea una instancia de Sequential
    assert isinstance(modelo, Sequential)

    # Verificar que la cantidad de capas del modelo sea 3
    assert len(modelo.layers) == 3

    # Verificar que la funcion de perdida del modelo sea la correcta
    assert modelo.loss == 'binary_crossentropy'