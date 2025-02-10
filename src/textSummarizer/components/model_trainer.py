import os
import gc
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from datasets import load_from_disk

from src.textSummarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        print(f"Config from ModelTrainer: {config}")
    def start_training(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        # print(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)
        
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        training_args = TrainingArguments(
            output_dir = self.config.output_dir,
            num_train_epochs = self.config.num_train_epochs,
            per_device_train_batch_size = self.config.per_device_train_batch_size,
            per_device_eval_batch_size = self.config.per_device_eval_batch_size,
            logging_dir = self.config.logging_dir,
            logging_steps = self.config.logging_steps,
            evaluation_strategy = self.config.evaluation_strategy,
            eval_steps = self.config.eval_steps,
            save_steps = self.config.save_steps,
            gradient_accumulation_steps = self.config.gradient_accumulation_steps,
            warmup_steps = self.config.warmup_steps,
            weight_decay = self.config.weight_decay
        )
        
        trainer = Trainer(
            model = model,
            args = training_args,
            data_collator = data_collator,
            train_dataset = dataset_samsum_pt['test'],
            eval_dataset = dataset_samsum_pt['validation']
        )
        
        trainer.train()
        
        model.save_pretrained(os.path.join(self.config.root_dir, "trained-pegausus-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "trained-pegausus-tokenizer"))
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()
        del model, tokenizer, data_collator, trainer, training_args