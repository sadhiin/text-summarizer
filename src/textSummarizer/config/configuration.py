import os
from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataIngestionConfig, DataTrasformationConfig, ModelTrainerConfig
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
    
    def get_data_transformation_config(self)-> DataTrasformationConfig:
        try:
            config = self.config.data_transformation
            
            os.makedirs(self.config.artifact_root, exist_ok=True)
            
            return DataTrasformationConfig(
                root_dir = config.root_dir,
                data_path = config.data_path,
                tokenizer_name = config.tokenizer_name
            )
        except Exception as e:
            logger.error(f"Error in creating DataTransformationConfig: {e}")
            return None
        
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        try:
            config = self.config.model_trainer
            params = self.params.TrainingArguments
            
            os.makedirs(config.root_dir, exist_ok=True)
            print(f"Config from Configmanager: {config}")
            
            return ModelTrainerConfig(
                root_dir = config.root_dir,
                data_path = config.data_path,
                model_ckpt = config.model_ckpt,
                output_dir = params.output_dir,
                num_train_epochs = params.num_train_epochs,
                warmup_steps = params.warmup_steps,
                per_device_train_batch_size = params.per_device_train_batch_size,
                per_device_eval_batch_size = params.per_device_eval_batch_size,
                logging_dir = params.logging_dir,
                weight_decay = params.weight_decay,
                logging_steps = params.logging_steps,
                evaluation_strategy = params.evaluation_strategy,
                eval_steps = params.eval_steps,
                save_steps = params.save_steps,
                gradient_accumulation_steps = params.gradient_accumulation_steps
            )
        except Exception as e:
            logger.error(f"Error in creating ModelTrainerConfig: {e}")
            return None