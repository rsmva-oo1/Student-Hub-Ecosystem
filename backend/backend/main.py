from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Student Hub Ecosystem API")

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "https://studenthub-ecosystem-hhza.vercel.app",  # Sizning Vercel manzilingiz
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/status")
def get_status():
    return {
        "status": "Online",
        "database": "Connected",
        "latency": "24ms"
    }

@app.get("/api/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "FastAPI integratsiyasi", "completed": True},
        {"id": 2, "title": "Vue premium dashboard dizayni", "completed": False},
        {"id": 3, "title": "Ma'lumotlar bazasini ulash", "completed": False}
    ]