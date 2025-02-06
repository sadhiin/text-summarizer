import os
import yaml
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from src.textSummarizer.logging import create_logger
from typing import Any, Dict, List, Union, Optional

logger = create_logger(__name__)


@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """
    Read yaml file and return as ConfigBox object
    """
    try:
        with open(path_to_yaml, 'r') as stream:
            config = yaml.safe_load(stream)
            return ConfigBox(config)
    except BoxValueError as e:
        logger.error(f"Error validating yaml file: {e}")
        return None
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")
        return None

@ensure_annotations
def create_directories(dirs: List[Path])->None:
    """
    Create directories if they do not exist
    """
    try:
        for dir in dirs:
            os.makedirs(dir, exist_ok=True)
            logger.info(f"Directory created: {dir}")
    
    except Exception as e:
        logger.error(f"Error creating directories: {e}")