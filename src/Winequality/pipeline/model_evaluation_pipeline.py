from src.Winequality.config.configuration import ConfigurationManager
from src.Winequality.components.model_evaluation import ModelEvaluation
from src.Winequality import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTraningPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_cofig = config.get_model_evaluation_config()
        model_evaluation_cofig = ModelEvaluation(config=model_evaluation_cofig)
        model_evaluation.log_into_mlflow()