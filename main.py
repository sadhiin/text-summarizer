from src.textSummarizer.pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline import DataTransformationPipeline
from src.textSummarizer.logging import create_logger
logger = create_logger(__name__)


def main():
    try:
        STAGE_NAME = "Data Ingestion Stage"
        logger.info(f"🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️ Starting {STAGE_NAME} 🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info(f"✅✅✅ Completed {STAGE_NAME} ✅✅✅")
        
        
        STAGE_NAME = "Data Trasnformation Stage"
        logger.info(f"🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️ Starting {STAGE_NAME} 🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️")
        pipeline = DataTransformationPipeline()
        pipeline.run()
        logger.info(f"✅✅✅ Completed {STAGE_NAME} ✅✅✅")
        
        
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

if __name__ == "__main__":
    main()