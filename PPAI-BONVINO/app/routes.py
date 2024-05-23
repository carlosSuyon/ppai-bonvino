# app/routes.py
from app import app
from app.controllers.gestor import obtener_ejemplo

@app.route('/ejemplo', methods=['GET'])
def ejemplo():
    return obtener_ejemplo()
