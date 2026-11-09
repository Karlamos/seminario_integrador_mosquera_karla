# app/main.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str 


@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "autor"  : "Karla Mosquera",
            "version": "0.1.0"}
        
@router.get("/karla")
def endpoint_karla() -> Mensaje:
    return Mensaje(texto="Hola", campo_interno="desde Karla link")

@router.get("/mosquera", response_model=Mensaje)
def endpoint_mosquera():
    return {"texto": "Hola", 
            "prioridad": 5, 
            "campo_interno": "imprime desde endpoint Mosquera"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra": "no debería salir"}