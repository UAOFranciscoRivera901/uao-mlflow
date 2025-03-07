from src.ml_flow.ml_flow_model import MODELOS
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def test_modelos():
    # Obtener la informacion del primer modelo
    nombre, parametros, modelo = obtener_informacion_modelo(0)
    # Verificar que sea correcta la informacion del primer modelo
    assert nombre == "Regresion_Logistica"
    assert isinstance(parametros, dict)
    assert isinstance(modelo, LogisticRegression)

    # Obtener la informacion del segundo modelo
    nombre, parametros, modelo = obtener_informacion_modelo(1)
    # Verificar que sea correcta la informacion del segundo modelo
    assert nombre == "Arbol_Decision"
    assert isinstance(parametros, dict)
    assert isinstance(modelo, DecisionTreeClassifier)

    # Obtener la informacion del tercer modelo
    nombre, parametros, modelo = obtener_informacion_modelo(2)
    # Verificar que sea correcta la informacion del tercer modelo
    assert nombre == "Bosque_Aleatorio"
    assert isinstance(parametros, dict)
    assert isinstance(modelo, RandomForestClassifier)

# Funcion para obtener la informacion de un modelo definido por el index
def obtener_informacion_modelo(index):
    modelo_completo = MODELOS[index]
    nombre = modelo_completo[0]
    parametros = modelo_completo[1]
    modelo = modelo_completo[2]
    return nombre, parametros, modelo