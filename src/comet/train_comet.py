import comet_ml
from src.comet.config_comet import COMET_API_KEY, PROJECT_NAME, WORKSPACE, PARAMS
from sklearn.metrics import log_loss
from src.evaluate import calcular_metricas,guardar_matriz_confusion

def entrenar_modelo(model_name, model, X_train, X_test, y_train, y_test):
    # Iniciar experimento en Comet ML
    experiment = comet_ml.Experiment(api_key=COMET_API_KEY, project_name=PROJECT_NAME, workspace=WORKSPACE)
    experiment.set_name(model_name)
    experiment.log_parameters(PARAMS)  # Registrar parámetros

    for i in range(100):
        experiment.set_step(i)

        if model_name == "RED_NEURONAL":
            history = model.fit(X_train, y_train, epochs=1, verbose=0, batch_size=PARAMS["batch_size"], validation_data=(X_test, y_test))
            loss_train = history.history["loss"][-1]
            loss_test = history.history["val_loss"][-1]
            y_test_proba = model.predict(X_test).flatten()
            y_pred = (y_test_proba > 0.5).astype(int)

        elif model_name == "RANDOM_FOREST":
            model.set_params(n_estimators=model.n_estimators + 1)
            model.fit(X_train, y_train)
            y_train_proba = model.predict_proba(X_train)[:, 1]
            y_test_proba = model.predict_proba(X_test)[:, 1]
            y_pred = model.predict(X_test)
            loss_train = log_loss(y_train, y_train_proba)
            loss_test = log_loss(y_test, y_test_proba)

        else:  # LOGISTIC_REGRESSION
            model.fit(X_train, y_train)
            y_train_proba = model.predict_proba(X_train)[:, 1]
            y_test_proba = model.predict_proba(X_test)[:, 1]
            y_pred = model.predict(X_test)
            loss_train = log_loss(y_train, y_train_proba)
            loss_test = log_loss(y_test, y_test_proba)

            
        # Calcular las diferentes metricas
        accuracy, precision, f1, recall, cm = calcular_metricas(y_test, y_pred)

        if i % 10 == 0:
            experiment.log_metric(f"{model_name}_accuracy", accuracy, step=i)
            experiment.log_metric(f"{model_name}_recall", recall, step=i)
            experiment.log_metric(f"{model_name}_precision", precision, step=i)
            experiment.log_metric(f"{model_name}_fscore", f1, step=i)
            experiment.log_metric(f"{model_name}_loss_train", loss_train, step=i)
            experiment.log_metric(f"{model_name}_loss_test", loss_test, step=i)

    # Registrar matriz de confusión una sola vez al final
    guardar_matriz_confusion(cm, model_name)
    experiment.log_confusion_matrix(matrix=cm, labels=["legitimate", "phishing"])

    experiment.end()  # Finalizar experimento
