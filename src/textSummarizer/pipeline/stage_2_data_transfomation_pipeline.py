from src.textSummarizer.config.configuration import CofigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.logging import create_logger

logger = create_logger(__name__)

class DataTransformationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = CofigurationManager()

        data_transformation_config = config.get_data_transformation_config()

        data_transformation = DataTransformation(data_transformation_config)

        data_transformation.convert()