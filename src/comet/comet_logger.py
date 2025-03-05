from comet_ml import Experiment
from src.config import API_KEY, EXPERIMENT_NAME, WORKSPACE

def iniciar_experimento():
    experiment = Experiment(
        api_key=API_KEY,
        project_name=EXPERIMENT_NAME,
        workspace=WORKSPACE
    )
    return experiment