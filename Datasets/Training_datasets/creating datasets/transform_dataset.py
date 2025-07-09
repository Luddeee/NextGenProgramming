import json

def transform_to_original_format(example):
    """
    Converts a single example dict from the new/expanded format
    to the old format with:
      {
        "question": ...,
        "expected_code": ...
      }
    Adjust this function as needed to suit your schema.
    """

    question_text = example.get("question", "")
    code = ""

    # "solutions" might be a string containing a JSON array
    if "solutions" in example and example["solutions"]:
        try:
            # Attempt to parse if it's a string
            solutions_list = json.loads(example["solutions"])
            # Option A: pick the first solution
            code = solutions_list[0] if solutions_list else ""

            # Option B (uncomment to combine solutions into one)
            # code = "\n# -- Alternative solution --\n".join(solutions_list)

        except json.JSONDecodeError:
            # If "solutions" isn't valid JSON or can't be parsed
            code = ""
    else:
        # If "solutions" is missing or empty
        code = ""

    # Return the "old" format
    return {
        "question": question_text,
        "expected_code": code
    }

def convert_jsonl_file(input_path, output_path):
    """
    Reads the input JSONL file line by line, transforms each record,
    then writes the transformed record to the output JSONL file.
    """
    with open(input_path, "r", encoding="utf-8") as fin, \
         open(output_path, "w", encoding="utf-8") as fout:
        
        for line in fin:
            # 1. Parse the JSON line into a dict
            record = json.loads(line)

            # 2. Transform record
            new_record = transform_to_original_format(record)

            # 3. Write the updated record to output JSONL
            json.dump(new_record, fout, ensure_ascii=False)
            fout.write("\n")

if __name__ == "__main__":
    # 1) Specify the path to your original expanded JSONL
    input_file = "my_large_dataset.jsonl"
    # 2) The path where you want the transformed dataset
    output_file = "my_transformed_dataset.jsonl"
    
    # Run the conversion
    convert_jsonl_file(input_file, output_file)
    
    print(f"Transformed dataset saved to: {output_file}")
