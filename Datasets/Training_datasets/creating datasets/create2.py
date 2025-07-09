# 1. Install and import


from datasets import load_dataset
import json

# 2. Load the MBPP dataset (train split as an example)
mbpp_train = load_dataset("mbpp", split="train")

print(f"Number of MBPP train examples: {len(mbpp_train)}")
print("First raw entry:", mbpp_train[0])  # show how it looks

# 3. Transform function
def transform_mbpp(example):
    # The MBPP dataset typically has fields: "text", "code", "test_list", ...
    # We'll rename "text" -> "question" and "code" -> "expected_code"
    question = example["text"].strip() if example["text"] else ""
    expected_code = example["code"].strip() if example["code"] else ""
    return {
        "question": question,
        "expected_code": expected_code
    }

# 4. Map transformation over the dataset
mbpp_formatted = mbpp_train.map(transform_mbpp)

# 5. (Optional) Print a few transformed samples to confirm
for i in range(3):  # print first 3
    print(mbpp_formatted[i])

# 6. Export to JSONL
output_file = "mbpp_formatted.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for ex in mbpp_formatted:
        json.dump(ex, f, ensure_ascii=False)
        f.write("\n")

print(f"MBPP data transformed and saved to '{output_file}'!")
