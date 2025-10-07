from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar templates (HTML)
templates = Jinja2Templates(directory="templates")

# Datos simulados (ejemplo)
procesos = [
    {"pid": 1001, "programa": "firefox", "estado": "Ejecutando", "prioridad": 0, "quantum": 50, "tiempo": 1250},
    {"pid": 1002, "programa": "vscode", "estado": "Listo", "prioridad": -5, "quantum": 75, "tiempo": 890},
    {"pid": 1003, "programa": "chrome", "estado": "Ejecutando", "prioridad": 2, "quantum": 40, "tiempo": 2100},
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "procesos": procesos})