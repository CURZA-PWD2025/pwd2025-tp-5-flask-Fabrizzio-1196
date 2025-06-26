from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola, soy Fabricio Abello. Soy estudiante de la tecnicatura en desarrollo web y estoy aprendiendo Flask.</h1>"

@app.route("/productos")
def listar_productos():
    salida = ""
    for p in productos:
        salida += f"ID: {p['id']} - Descripción: {p['descripcion']} - Categoría ID: {p['categoria_id']}<br>"
    return salida

@app.route("/categorias")
def listar_categorias():
    salida = ""
    for c in categorias:
        salida += f"ID: {c['id']} - Descripción: {c['descripcion']}<br>"
    return salida

if __name__ == "__main__":
    app.run(debug=True)




