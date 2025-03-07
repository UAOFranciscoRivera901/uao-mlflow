from src.comet.config_comet import PARAMS, COMET_API_KEY, PROJECT_NAME, WORKSPACE

def test_params():
    # Verificar que los parametros sean los correctos
    assert PARAMS["neuronas"] == 64
    assert PARAMS["activacion"] == "relu"
    assert PARAMS["optimizador"] == "RMSprop"
    assert PARAMS["batch_size"] == 32
    assert PARAMS["max_depth"] == 3

def test_configuracion():
    # Verificar que los datos que necesita Comet-Ml sean los correctos
    assert COMET_API_KEY == "zf9t8KH3vUJq9o3PraFgGtfOX"
    assert PROJECT_NAME == "phishing-detection"
    assert WORKSPACE == "anfeco20"