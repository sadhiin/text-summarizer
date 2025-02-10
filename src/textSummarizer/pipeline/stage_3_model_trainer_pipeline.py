from src.textSummarizer.config.configuration import CofigurationManager
from src.textSummarizer.components.model_trainer import ModelTrainer
from src.textSummarizer.logging import create_logger

logger = create_logger(__name__)

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def run(self):
        config = CofigurationManager()

        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(model_trainer_config)

        model_trainer.start_training()
        