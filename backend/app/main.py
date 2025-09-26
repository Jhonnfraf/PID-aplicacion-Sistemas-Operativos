# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil

app = FastAPI()

# Permitir llamadas desde Angular (http://localhost:4200)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cpu")
def get_cpu():
    return {"cpu_percent": psutil.cpu_percent(interval=1)}

@app.get("/memory")
def get_memory():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "available": mem.available,
        "percent": mem.percent
    }