import os
from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataIngestionConfig
from src.textSummarizer.logging import create_logger
logger = create_logger(__name__)

class CofigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_filepath)

        # create_directories([self.config.artifact_root])
        os.makedirs(self.config.artifact_root, exist_ok=True)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion
            
            # Ensure that the root directory for data ingestion exists
            # create_directories([config.root_dir])
            os.makedirs(config.root_dir, exist_ok=True)
            return DataIngestionConfig(
                root_dir=config.root_dir,
                source_uri=config.source_uri,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )
        except AttributeError as e:
            logger.error(f"Missing data ingestion configuration: {e}")
            return None
        except Exception as e:
            logger.error(f"Error in creating DataIngestionConfig: {e}")
            return None
