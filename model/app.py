from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load lightweight model
MODEL_NAME = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

from pyngrok import ngrok

app = Flask(__name__)

def generate_text(prompt, temperature=0.7, top_p=0.9, max_length=100):
    input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"]
    outputs = model.generate(input_ids, max_length=max_length, temperature=temperature, top_p=top_p)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    if "prompt" not in data:
        return jsonify({"error": "Missing prompt"}), 400

    prompt = data["prompt"]
    response = generate_text(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)