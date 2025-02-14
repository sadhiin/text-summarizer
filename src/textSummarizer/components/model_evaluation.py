import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import pandas as pd
from tqdm import tqdm
from src.textSummarizer.entity import ModelEvaluationConfig
import evaluate

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
    def generate_batch_sized_chunks(self, list_of_elements, batch_size):

        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i:i+batch_size]

    def calculate_metric_on_test_data(self,dataset, metric, model, tokenizers,
                                    batch_size=16, column_text='article', column_summary="summary"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        summary_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, summary_batch in tqdm(zip(article_batches, summary_batches), total=len(article_batches)):
            # inputs = tokenizers(article_batch, max_length=1024, return_tensors='pt', truncation=True, padding=True).to(self.device)
            # outputs = model.generate(**inputs)
            # predictions = tokenizers.batch_decode(outputs, skip_special_tokens=True)
            # metric.add_batch(predictions=predictions, references=summary_batch)

            inputs = self.tokenizer(article_batch, max_length=1024, truncation=True, padding=True, return_tensors='pt').to(self.device)

            summaries = model.generate(input_ids = inputs["input_ids"].to(self.device),
                                    attention_mask=inputs['attention_mask'].to(self.device),
                                    length_penalty=0.8, num_beams=9, max_length=128)
            """ parameter for length penalty to avoid the too long sequence to generate the model """

            decode_summaries = [self.tokenizer.decode(s, skip_special_tokens=True,clean_up_tokenization_spaces=True)
                                for s in summaries]
            decode_summaries = [d.replace('', ' ') for d in decode_summaries]
            metric.add_batch(predictions=decode_summaries, references=summary_batch)

        score = metric.compute()
        return score
    
    def evaluate(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.dataset = load_from_disk(self.config.data_path)
        
        rouge_names = ['rouge1', 'rouge2', 'rougeL', 'rougeLsum']
        rouge_metric = evaluate.load('rouge')
        
        score = self.calculate_metric_on_test_data(
            self.dataset['train'][0:5],
            rouge_metric, self.model, self.tokenizer, batch_size=16, column_text='dialogue', column_summary='summary')
        print("Sore: ", score)
        rouge_dict = {rn: score[rn] for rn in rouge_names}
        df = pd.DataFrame(rouge_dict, index=['pegasus'])
        
        df.to_csv(self.config.metric_file_name)