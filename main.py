from src.textSummarizer.pipeline.stage_1_data_ingestion_pipline import DataIngestionPipeline
from src.textSummarizer.logging import create_logger
logger = create_logger(__name__)

STAGE_NAME = "Data Ingestion Stage"

def main():
    try:
        logger.info(f"🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️ Starting {STAGE_NAME} 🏃🏼‍➡️🏃🏼‍➡️🏃🏼‍➡️")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info(f"✅✅✅ Completed {STAGE_NAME} ✅✅✅")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

if __name__ == "__main__":
    main()