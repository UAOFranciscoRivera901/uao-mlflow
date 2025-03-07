from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

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
