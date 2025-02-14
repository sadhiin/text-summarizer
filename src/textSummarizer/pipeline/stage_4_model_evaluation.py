from src.textSummarizer.config.configuration import CofigurationManager
from src.textSummarizer.components.model_evaluation import ModelEvaluation
from src.textSummarizer.logging import create_logger

logger = create_logger(__name__)

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = CofigurationManager()

        model_evaluation_config = config.get_model_evaluation_config()

        model_evaluation = ModelEvaluation(model_evaluation_config)

        model_evaluation.evaluate()