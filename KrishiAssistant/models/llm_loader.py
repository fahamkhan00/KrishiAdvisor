# models/llm_loader.py

from llama_cpp import Llama
import os

MODEL_PATH = os.path.expanduser(
    "~/KrishiAdvisorApp/KrishiAssistant/llama.cpp/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
)

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,  # Adjust based on your CPU cores
    n_batch=64,
    verbose=False
)

def load_llm():
    return llm










'''
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_llm(model_id="mistralai/Mistral-7B-Instruct-v0.1"):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=150)
    return pipe
'''
