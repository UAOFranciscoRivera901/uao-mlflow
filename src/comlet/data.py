from datasets import load_dataset
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

def cargar_datos():
    dataset = load_dataset("pirocheto/phishing-url")

    df_train = pd.DataFrame(dataset['train'])
    df_test = pd.DataFrame(dataset['test'])

    X_train = df_train.drop(columns=['url', 'status'])
    y_train = df_train['status'].values

    X_test = df_test.drop(columns=['url', 'status'])
    y_test = df_test['status'].values

    encoder = LabelEncoder()
    y_train = encoder.fit_transform(y_train)
    y_test = encoder.transform(y_test)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test