import requests

def obtener_contenido_wikipedia(busqueda):
    try:
        # Hacer la solicitud a la API de Wikipedia para buscar el título del artículo
        url_busqueda = f"https://es.wikipedia.org/w/api.php?action=query&list=search&srsearch={busqueda}&format=json"
        response = requests.get(url_busqueda)
        response.raise_for_status()  # Lanza una excepción en caso de error

        data = response.json()
        if "query" in data and "search" in data["query"]:
            if data["query"]["search"]:
                # Obtener el título del primer resultado de búsqueda
                titulo_articulo = data["query"]["search"][0]["title"]

                # Hacer una solicitud para obtener toda la información del artículo
                url_info = f"https://es.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&explaintext&titles={titulo_articulo}"
                response = requests.get(url_info)
                response.raise_for_status()  # Lanza una excepción en caso de error

                data = response.json()
                if "query" in data and "pages" in data["query"]:
                    # Obtener el contenido completo del artículo
                    pagina = next(iter(data["query"]["pages"].values()))
                    contenido = pagina.get("extract", "No se encontró contenido.")
                    return contenido
                else:
                    return "Error al obtener información del artículo de Wikipedia."
            else:
                return "No se encontraron resultados en Wikipedia para la búsqueda."
        else:
            return "Error al buscar el título del artículo en Wikipedia."
    except requests.exceptions.RequestException as e:
        return f"Error en la solicitud a la API de Wikipedia: {str(e)}"

# Ejemplo de uso de la función
# busqueda = "vida"
# contenido = obtener_contenido_wikipedia(busqueda)

# print(limpiar_palabras.limpiar_palabras_clave(obtener_palabras_claves.obtener_palabras_clave(contenido)))
# print(contenido)

'''
cercania de las palabras 
como medir distancia con emvedings
'''