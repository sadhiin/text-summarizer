from src.textSummarizer.config.configuration import CofigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.logging import create_logger
logger = create_logger(__name__)

class DataIngestionPipeline:
    def __init__(self):
        pass
    def run(self):
        config = CofigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)

        data_ingestion.download_data()
        data_ingestion.extract_zip_file()