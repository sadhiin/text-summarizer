from src.textSummarizer.pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline import ModelEvaluationPipeline
from src.textSummarizer.logging import create_logger
logger = create_logger(__name__)
import torch
import gc

def main():
    try:
        STAGE_NAME = "Data Ingestion Stage"
        logger.info(f"🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️ Starting {STAGE_NAME} 🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info(f"✅✅✅ Completed {STAGE_NAME} ✅✅✅")
        
        gc.collect()
        
        STAGE_NAME = "Data Trasnformation Stage"
        logger.info(f"🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️ Starting {STAGE_NAME} 🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️")
        pipeline = DataTransformationPipeline()
        pipeline.run()
        logger.info(f"✅✅✅ Completed {STAGE_NAME} ✅✅✅")
        
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        STAGE_NAME = "Model Training Stage"
        logger.info(f"🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️ Starting {STAGE_NAME} 🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️")
        pipeline = ModelTrainerPipeline()
        pipeline.run()
        logger.info(f"✅✅✅ Completed {STAGE_NAME} ✅✅✅")
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        STAGE_NAME = "Model Evaluation Stage"
        logger.info(f"🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️ Starting {STAGE_NAME} 🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️")
        pipeline = ModelEvaluationPipeline()
        pipeline.run()
        logger.info(f"✅✅✅ Completed {STAGE_NAME} ✅✅✅")
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

if __name__ == "__main__":
    main()