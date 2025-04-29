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
    Endpoint raiz que devuelve una respuesta JSON simple.
    """
    return {"Biometrico": "ok"}

from routes.python_lambda import *

# Configurar Mangum para funcionar con Lambda
handler = Mangum(app)