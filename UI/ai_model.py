from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import logging

# Load the trained model and tokenizer
MODEL_PATH = "./AI models/expanded_trained_codet5"

logging.debug("Loading the trained model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

def translate_to_python(math_problem: str) -> str:
    try:
        logging.debug(f"Translating problem: {math_problem}")
        inputs = tokenizer(math_problem, return_tensors="pt", truncation=True, max_length=128)
        outputs = model.generate(inputs.input_ids, max_length=128, num_beams=5, early_stopping=True)
        python_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return python_code
    except Exception as e:
        logging.error(f"Error in translation: {str(e)}")
        return f"Error: {str(e)}"
