import json

input_file = "mbpp_formatted.jsonl"      # The file with all fields (task_id, text, etc.)
output_file = "converted.jsonl"   # The new file with only question & expected_code

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        # Parse each line as JSON
        record = json.loads(line)

        # Create a new minimal dict
        minimal_record = {
            "question": record["question"],
            "expected_code": record["expected_code"]
        }

        # Write it as a single JSON object per line
        json.dump(minimal_record, fout, ensure_ascii=False)
        fout.write("\n")

print(f"Created '{output_file}' with only 'question' and 'expected_code' fields.")
