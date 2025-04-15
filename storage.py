import json
import os

DATA_FILE = "students.json"

def load_student_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_student_data(students):
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)