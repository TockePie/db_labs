from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "feedbacks.json"


class Feedback(BaseModel):
    id: int
    name: str
    comment: str

feedbacks = []


def load_feedbacks():
    global feedbacks
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            feedbacks_data = json.load(f)
            feedbacks = [Feedback(**item) for item in feedbacks_data]

def save_feedbacks():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([fb.dict() for fb in feedbacks], f, ensure_ascii=False, indent=4)

@app.on_event("startup")
def startup_event():
    load_feedbacks()

@app.get("/")
def read_root():
    return {"message": "Привіт від FastAPI"}

@app.get("/feedback")
def get_feedback():
    return feedbacks

@app.post("/feedback")
def create_feedback(item: Feedback):
    feedbacks.append(item)
    save_feedbacks()
    return {"message": "Фідбек додано", "data": item}
