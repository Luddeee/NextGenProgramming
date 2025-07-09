# Step 1: Install and Import

from datasets import load_dataset
import json

# Step 2: Load the APPS "train" split


apps_train = load_dataset("codeparrot/apps", "all")

# Step 3: Transform function
def transform_apps(example):
    # example["solutions"] is a list. We'll pick the first solution for 'expected_code'.
    if example["solutions"]:
        code = example["solutions"][0]
    else:
        code = ""
    return {
        "question": example["question"],
        "expected_code": code
    }

# Step 4: Map transformation
apps_formatted = apps_train.map(transform_apps)

# Step 5: Export to JSONL
with open("my_large_dataset.jsonl", "w", encoding="utf-8") as f:
    for ex in apps_formatted:
        json.dump(ex, f, ensure_ascii=False)
        f.write("\n")

print("Dataset created: my_large_dataset.jsonl")
