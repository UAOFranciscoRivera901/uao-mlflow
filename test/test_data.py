from src.data import cargar_datos

def test_cargar_datos():
    # Obtener los datos del metodo que se va a probar
    X_train, X_test, y_train, y_test = cargar_datos()

    # Verificar que haya obtenido datos de entrenamiento y de prueba
    assert X_train.shape[0] > 0, "X_train no debe estar vacío"
    assert X_test.shape[0] > 0, "X_test no debe estar vacío"

    # Verificar que las X y las y tengan la misma cantidad de filas
    assert len(y_train) == X_train.shape[0], "y_train debe tener las mismas filas que X_train"
    assert len(y_test) == X_test.shape[0], "y_test debe tener las mismas filas que X_test"