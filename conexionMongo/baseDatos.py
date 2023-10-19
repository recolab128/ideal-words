from pymongo import MongoClient

def conectar_mongodb(url, nombre_base_datos):
    try:
        # Crea una instancia de cliente de MongoDB
        client = MongoClient(url)

        # Selecciona la base de datos
        db = client[nombre_base_datos]
        print('se logro')
        return db
    except Exception as e:
        print(f"Error al conectar a MongoDB: {str(e)}")
        return None

def mostrar_contenido_Coleccion(coleccion):
    documentos = coleccion.find()
    # Imprimir el contenido de cada documento
    for documento in documentos:
        print(documento)


def insertar_en_coleccion(conexion, nombre_coleccion, datos):

    try:
        # Accede a la colección utilizando la conexión
        coleccion = conexion[nombre_coleccion]

        # Realiza la inserción de los datos
        resultado = coleccion.insert_one(datos)

        # Devuelve el ID del documento insertado
        return resultado.inserted_id
    except Exception as e:
        print(f"Error al insertar en la colección: {str(e)}")
        return None

from pymongo import MongoClient

def eliminar_documentos_coleccion(database_url, database_name, collection_name):
    try:
        # Conéctate a la base de datos y colección
        client = MongoClient(database_url)
        db = client[database_name]
        coleccion = db[collection_name]

        # Elimina todos los documentos de la colección
        resultado = coleccion.delete_many({})

        # Devuelve el número de documentos eliminados
        return resultado.deleted_count

    except Exception as e:
        print(f"Error al eliminar documentos: {str(e)}")
        return 0  # Retorna 0 si se produce un error

    finally:
        # Cierra la conexión con MongoDB
        if 'client' in locals():
            client.close()

#    g.mongo = baseDatos.conectar_mongodb('mongodb+srv://leonel:root123@cluster0.0zpr9n7.mongodb.net/?retryWrites=true&w=majority', 'recolab-innovatecnm')

# # Ejemplo de uso:
# if __name__ == "__main__":
#     url_mongo = 'mongodb+srv://leonel:root123@cluster0.0zpr9n7.mongodb.net/?retryWrites=true&w=majority'  # Reemplaza con tu URL de MongoDB
#     nombre_bd = 'recolab-innovatecnm'
#     nombre_coleccion = 'words'

#     num_documentos_eliminados = eliminar_documentos_coleccion(url_mongo, nombre_bd, nombre_coleccion)
#     print(f"Se eliminaron {num_documentos_eliminados} documentos en la colección {nombre_coleccion}.")
