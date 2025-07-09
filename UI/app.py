import os
import logging
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///math_translations.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
db.init_app(app)

from models import MathProblem
from ai_model import translate_to_python
from code_executor import execute_python_code

@app.route('/')
def index():
    example_problems = [
        "Solve 5 + 9",
        "what is the product of 4 and 9",
        "take the square root of 56",
        "what is 9 squared",
        "What is 8 plus 9 plus 10"
    ]
    return render_template('index.html', example_problems=example_problems)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        math_problem = request.form.get('problem', '').strip()
        if not math_problem:
            return jsonify({'error': 'No problem provided'}), 400

        if len(math_problem) > 256:
            return jsonify({'error': 'Input too long'}), 400

        # Generate Python code from the problem
        python_code = translate_to_python(math_problem)
        if not python_code:
            return jsonify({'error': 'Failed to generate Python code'}), 400

        

        # Save the result to the database
        try:
            new_problem = MathProblem(
                problem_text=math_problem,
                generated_code=python_code,
                
            )
            db.session.add(new_problem)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(f"Database error: {str(e)}")
            return jsonify({'error': 'Failed to save the problem'}), 500

        # Return code
    
        return jsonify({
            'code': python_code,
        })

    except Exception as e:
        logging.error(f"Error processing translation: {str(e)}")
        return jsonify({'error': str(e)}), 500


with app.app_context():
    db.create_all()
