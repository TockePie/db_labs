from fastapi import FastAPI, HTTPException
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
    return {"message": "олєлє олала"}

@app.get("/feedback")
def get_feedback():
    return feedbacks

@app.post("/feedback")
def create_feedback(item: Feedback):
    for fb in feedbacks:
        if fb.id == item.id:
            raise HTTPException(status_code=400, detail="Фідбек з таким ID вже існує")
    feedbacks.append(item)
    save_feedbacks()
    return {"message": "Фідбек додано", "data": item}

@app.put("/feedback/{feedback_id}")
def update_feedback(feedback_id: int, item: Feedback):
    for index, fb in enumerate(feedbacks):
        if fb.id == feedback_id:
            feedbacks[index] = item
            save_feedbacks()
            return {"message": "Фідбек оновлено", "data": item}
    raise HTTPException(status_code=404, detail="Фідбек не знайдено")

@app.delete("/feedback/{feedback_id}")
def delete_feedback(feedback_id: int):
    for index, fb in enumerate(feedbacks):
        if fb.id == feedback_id:
            deleted = feedbacks.pop(index)
            save_feedbacks()
            return {"message": "Фідбек видалено", "data": deleted}
    raise HTTPException(status_code=404, detail="Фідбек не знайдено")


@app.get("/feedback/{feedback_id}")
def get_feedback_by_id(feedback_id: int):
    for fb in feedbacks:
        if fb.id == feedback_id:
            return fb
    raise HTTPException(status_code=404, detail="Фідбек не знайдено")