import json
from pathlib import Path

CAMINHO_BANCO = Path(__file__).parent.parent / "esquema" / "restaurantes.json"

def ler_banco():
    with open(CAMINHO_BANCO, "r", encoding="utf-8") as f:
        return json.load(f)

def buscar_restaurante(nome):
    banco = ler_banco()
    for r in banco["restaurantes"]:
        if r["nome"].lower() == nome.lower():
            return r
    return None
