import random
from transformers import T5ForConditionalGeneration, RobertaTokenizer
import json
from sklearn.metrics import precision_score, recall_score, f1_score

#Load the model and tokenizer
model_name = "/Users/luddesmac/Desktop/Skola/TUM/Next-gen-prog/berlin/TestingCodeT5/trained_codet5" #Change for your path
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

#Load dataset
dataset_path = "/Users/luddesmac/Desktop/Skola/TUM/Next-gen-prog/berlin/Datasets/Testing_datasets/test_dataset.jsonl" #change for your path
data = []
with open(dataset_path, "r") as f:
    for line in f:
        data.append(json.loads(line))

#Tracking metrics
y_true = []
y_pred = []
correct = 0
total = len(data)

incorrect_samples = []

print("Testing CodeT5-trained")

for i, sample in enumerate(data):
    input_text = sample["question"]
    expected_output = sample["expected_code"].strip()

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    outputs = model.generate(input_ids, max_new_tokens=100)
    predicted_output = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    is_correct = int(predicted_output == expected_output)
    y_true.append(1)  #Correct answer label
    y_pred.append(is_correct)  #Model's prediction

    if is_correct:
        correct += 1
    else:
        incorrect_samples.append({
            "question": input_text,
            "expected": expected_output,
            "predicted": predicted_output
        })

    #Print progress every 100 examples
    if (i + 1) % 100 == 0:
        print(f"Processed {i + 1}/{total} examples...")

#evaluation metrics
accuracy = correct / total * 100
precision = precision_score(y_true, y_pred, average='binary')
recall = recall_score(y_true, y_pred, average='binary')
f1 = f1_score(y_true, y_pred, average='binary')

print(f"\nEvaluation Results:")
print(f"Accuracy: {accuracy:.2f}% ({correct}/{total})")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

#Manual
print("\n🔍 **Manual Inspection of Model Predictions** 🔍\n")
sample_cases = random.sample(data, 5)  #5 random cases

for i, sample in enumerate(sample_cases, 1):
    input_text = sample["question"]
    expected_output = sample["expected_code"].strip()

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    outputs = model.generate(input_ids, max_new_tokens=100)
    predicted_output = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    #Check if correct
    status = "Correct" if predicted_output == expected_output else "Incorrect"

    #Print result
    print(f"\n🔹 Example {i}:")
    print(f"  **Question:** {input_text}")
    print(f"  **Expected Output:** {expected_output}")
    print(f"  **Predicted Output:** {predicted_output}")
    print(f"  **Status:** {status}")
    print("-" * 50)

#Save incorrect stuff
if incorrect_samples:
    with open("incorrect_predictions.json", "w") as f:
        json.dump(incorrect_samples, f, indent=4)
    print("Incorrect predictions saved to 'incorrect_predictions.json' for further analysis.")
