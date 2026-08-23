from pathlib import Path
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="UrjaSahayak AI API",
    description="Energy supply-chain resilience prototype API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename: str):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


@app.get("/")
def home():
    return {
        "message": "Welcome to UrjaSahayak AI API",
        "status": "running"
    }


@app.get("/api/suppliers")
def get_suppliers():
    return load_json("suppliers.json")


@app.get("/api/routes")
def get_routes():
    return load_json("routes.json")


@app.get("/api/events")
def get_events():
    return load_json("sample_events.json")
