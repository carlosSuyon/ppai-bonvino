# app/__init__.py
from flask import Flask

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configurar la aplicación Flask (opcional)
app.config['SECRET_KEY'] = 'clave_secreta'  # Ejemplo de configuración

# Importar las rutas después de crear la aplicación
from app import routes
