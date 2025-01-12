# qa/ml/qa_model.py
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import torch

class QA_Model:
    def __init__(self, model_path="./fine_tuned_bert_merged"):
        self.model_path = model_path
        self.model, self.tokenizer, self.device = self.load_model()

    def load_model(self):
        model = AutoModelForQuestionAnswering.from_pretrained(self.model_path)
        tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = model.to(device)
        return model, tokenizer, device

    def answer_question(self, context, question):
        qa_pipeline = pipeline("question-answering", model=self.model, tokenizer=self.tokenizer)
        result = qa_pipeline(question=question, context=context)
        return result['answer']
