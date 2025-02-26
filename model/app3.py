from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "distilgpt2"  # Use a lightweight model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def generate_text(prompt, temperature=0.7, top_p=0.9, max_length=100):
    input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"]
    outputs = model.generate(input_ids, max_length=max_length, temperature=temperature, top_p=top_p)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test sample input
prompt = "Hello"
response = generate_text(prompt)
print(f"Prompt: {prompt}\nResponse: {response}")
