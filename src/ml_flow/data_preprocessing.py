import pandas as pd
from datasets import load_dataset
from sklearn.preprocessing import StandardScaler, LabelEncoder

def cargar_datos():
    """Carga y preprocesa los datos de entrenamiento y prueba."""
    dataset = load_dataset("pirocheto/phishing-url")

    df_train = pd.DataFrame(dataset['train'])
    X_train = df_train.drop(columns=['url', 'status'])
    y_train = df_train['status'].values

    df_test = pd.DataFrame(dataset['test'])
    X_test = df_test.drop(columns=['url', 'status'])
    y_test = df_test['status'].values

    # Convertir a valores numéricos
    encoder = LabelEncoder()
    y_train = encoder.fit_transform(y_train)
    y_test = encoder.transform(y_test)

    # Normalizar los datos
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, y_train, X_test, y_test
