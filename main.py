from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
    return {"status": "ok"}

todo_items = []
@app.post("/")
def add_item(request: dict):
    todo_items.append(request["item"]) # Adding item to our todo_items list
    return {"status": "ok", "message": "Item added"} #Sending the API Response back