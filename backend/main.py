from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"status": "Active", "project": "Student Hub API", "developer": "Rustamova Munisa"}
