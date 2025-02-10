import os
from src.textSummarizer.logging import create_logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.textSummarizer.entity import DataTrasformationConfig

class DataTransformation:
    def __init__(self, config: DataTrasformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
        self.logger = create_logger(self.__class__.__name__)
        
    def _conver_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], truncation=True, padding='max_length', max_length=1024)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], truncation=True, padding='max_length', max_length=128)

        encodings = {
            'input_ids': input_encodings.input_ids,
            'attention_mask': input_encodings.attention_mask,
            'labels': target_encodings.input_ids
        }
        return encodings

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self._conver_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset'))