import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import create_logger
import os
from urllib import request
from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.logger = create_logger(__name__)
        
    def download_data(self):
        try:
            # Check if the directory exists
            if not os.path.exists(self.config.local_data_file):
                self.logger.info(f"Creating the directory {self.config.local_data_file}")
                os.makedirs(self.config.local_data_file)

            # Define the file path where the data will be saved
            zip_file_path = os.path.join(self.config.local_data_file, "summarizer-data.zip")  # Specify the file name

            if not os.path.exists(zip_file_path):  # Check if the file already exists
                self.logger.info(f"Downloading data from {self.config.source_uri}")
                filename, headers = request.urlretrieve(
                    url=self.config.source_uri, 
                    filename=zip_file_path)  # Use the full path with the file name
            else:
                self.logger.info(f"File {zip_file_path} already exists")
            
        except Exception as e:
            self.logger.error(f"Error downloading data from {self.config.source_uri}")
            self.logger.error(e)
            raise e
    
    def extract_zip_file(self):
        try:
            # Ensure the extraction directory exists
            os.makedirs(self.config.unzip_dir, exist_ok=True)
            
            # Specify the correct file path for the downloaded zip file
            zip_file_path = os.path.join(self.config.local_data_file, "summarizer-data.zip")  # Correct zip file path

            # Use the correct file path to extract the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            self.logger.info(f"Extracting zip file to {self.config.unzip_dir}")
        except Exception as e:
            self.logger.error(f"Error extracting zip file to {self.config.unzip_dir}")
            self.logger.error(e)
            raise e
