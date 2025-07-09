from app import db
from datetime import datetime

class MathProblem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem_text = db.Column(db.Text, nullable=False)
    generated_code = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    def __init__(self, problem_text, generated_code):
        self.problem_text = problem_text
        self.generated_code = generated_code
