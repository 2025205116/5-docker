from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()
DATA_FILE = "courses.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.get("/courses")
def get_courses():
    with open(DATA_FILE, "r") as f:
        return json.load(f)