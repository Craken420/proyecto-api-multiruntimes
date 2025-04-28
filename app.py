# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# Crear la instamcia FastAPI
app = FastAPI()

# Agregar middleware CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    """
    Endpoint raíz que devuelve una respuesta JSON simple.
    """
    return {"Biometrico": "ok"}

@app.get("/huella")
def huella():
    """
    Endpoint para la ruta '/huella'.
    """
    return {"message": "Ruta de huella funcionando"}

# Configurar Mangum para funcionar con Lambda
handler = Mangum(app)