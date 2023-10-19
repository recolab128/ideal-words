from flask import Flask, render_template, request, g, redirect, url_for
from buscar_sustantivos import buscar_sustantivos
import baseDatos

app = Flask(__name__)

@app.before_request
def antes_de_la_solicitud():
    # Abre una conexión a MongoDB y la almacena en g.mongo
    g.mongo = baseDatos.conectar_mongodb('mongodb+srv://leonel:root123@cluster0.0zpr9n7.mongodb.net/?retryWrites=true&w=majority', 'recolab-innovatecnm')

@app.teardown_request
def despues_de_la_solicitud(exception=None):
    # Cierra la conexión a la base de datos al final de la solicitud
    if hasattr(g, 'mongo'):
        g.mongo.client.close()  # Cierra la conexión de la base de datos

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db = g.mongo
        tema = request.form.get('tema')
        documentos=db.words.count_documents({"concept": tema})
        print(documentos, tema)
        if documentos==0:
            resultados = buscar_sustantivos(tema)
            return render_template('guardarDatos.html', tema=tema, resultados=resultados)
        else:
            return render_template('index.html', Error= 'El concepto que intentas agregar ya ha sido registrado.')
    return render_template('index.html')

@app.route('/guardar_datos', methods=['GET', 'POST'])
def guardar_datos():
    if request.method == 'POST':
        db = g.mongo
        area = request.form.get('clasificaciones')
        tema = request.form.get('tema2')
        opciones_sugeridas = request.form.get('opciones_sugeridas').split(',')
        opciones = request.form.getlist('opciones[]')
        keywords = list(set(opciones + opciones_sugeridas))
        datos_a_insertar = {
            "area": area,
            "concept": tema,
            "keywords": keywords
        }
        print(datos_a_insertar,'asdsad')
        baseDatos.insertar_en_coleccion(db, 'words', datos_a_insertar)
        return redirect(url_for('index'))



@app.route('/mostrar_documentos', methods=['GET', 'POST'])
def mostrar_documentos():
    # Recupera los documentos de la colección "words" en MongoDB
    documentos = list(g.mongo.words.find())
    return render_template('mostrarDocumentos.html', resultado=documentos)


if __name__ == '__main__':
    app.run(debug=True)
