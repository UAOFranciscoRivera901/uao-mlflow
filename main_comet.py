import sys
import os

# Añadir src/comet al path de Python
sys.path.append(os.path.abspath("src/comet"))
from src.data import cargar_datos
from src.comet.models_comet import obtener_modelos
from src.comet.train_comet import entrenar_modelo


print("El script se está ejecutando correctamente")
def main():
    # Cargar y procesar los datos
    X_train, X_test, y_train, y_test = cargar_datos()

    # Obtener modelos
    modelos = obtener_modelos(input_dim=X_train.shape[1])

    # Entrenar cada modelo
    for nombre, modelo in modelos.items():
        entrenar_modelo(nombre, modelo, X_train, X_test, y_train, y_test)
        

if __name__ == "__main__":
    main()
