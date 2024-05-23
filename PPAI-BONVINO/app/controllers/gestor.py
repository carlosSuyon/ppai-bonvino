# app/controllers/gestor.py
from flask import jsonify

def obtener_ejemplo():
    # Lógica para obtener datos del modelo
    ejemplo = {"id": 1, "nombre": "Ejemplo"}
    return jsonify(ejemplo)
