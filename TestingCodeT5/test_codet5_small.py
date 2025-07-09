from transformers import T5ForConditionalGeneration, RobertaTokenizer
import json

# Load the model and tokenizer
model_name = "Salesforce/codeT5-small"
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Load your dataset
dataset_path = "/Users/casperkejser/Downloads/Training_dataset_expanded_15k.jsonl"  # Update with the correct path
data = []
with open(dataset_path, "r") as f:
    for line in f:
        data.append(json.loads(line))

# Testing the model
correct = 0
total = len(data)

print("Testing CodeT5-small...")
for i, sample in enumerate(data):
    input_text = sample["question"]
    expected_output = sample["expected_code"]

    # Tokenize input
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    # Generate output
    outputs = model.generate(input_ids)
    predicted_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Compare with expected output
    if predicted_output.strip() == expected_output.strip():
        correct += 1

    # Print progress every 100 examples
    if (i + 1) % 100 == 0:
        print(f"Processed {i + 1}/{total} examples...")

# Print results
accuracy = correct / total * 100
print(f"Accuracy: {accuracy:.2f}% ({correct}/{total})")

