# Math Prompt Translator

Math Prompt Translator is a Flask application containing a pretrained AI model and translating natural language math prompts into Python code.

## Features
- Translate natural language math prompts into Python code.
- Train your own model.
- Finetune existing models and test them.

## Installation
1. Clone with SSH:
```bash
git clone git@gitlab.lrz.de:bpc-ws-2425/berlin.git
cd berlin
```
or with HTTPS:
```bash
https://gitlab.lrz.de/bpc-ws-2425/berlin.git
cd berlin
```

Install the dependencies from the dependencies.txt file.
## Usage
For using the Flask application:
```bash
cd UI
python main.py
```
For training the base CodeT5 model use the TrainingModelCodeT5.ipynb notebook. Make sure to change the dataset you want to use in the second cell.

For fine-tuning an already existing local model use the finetyne.ipynb notebook and change the MODEL_DIR variable accordingly. Currently, the MODEL_DIR variable is set to expanded_trained_codet5 in the AI models folder. This model is trained with the combined.jsonl dataset, including APPS and MBPP datasets.

The trained_codet5 model in the AI models is the model containing the arithmetic operations, including operations with variables.
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Original authors
- Ludvig Sanell
- Boris Petreski
- Casper du Jardin Kejser

## License

[MIT] LICENSE.txt
