import gc
import torch
from transformers import pipeline, AutoTokenizer
from src.textSummarizer.config.configuration import CofigurationManager
from src.textSummarizer.logging import create_logger

logger = create_logger(__name__)

class PredictionPipeline:
    def __init__(self):
        self.config = CofigurationManager().get_model_evaluation_config()
        print(f"PredictionPipeline config: {self.config}")
    def prediction(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, 'num_beams':8, "max_length": 128}
        
        pipe = pipeline("summarization",
                        model=self.config.model_path, 
                        tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
        logger.info(f"Dialoge: {text}")
        
        output = pipe(text, **gen_kwargs)[0]['summary_text']
        logger.info(f"Model Summary: {output}")
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()
        return output