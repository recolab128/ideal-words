import re
import difflib

def limpiar_palabras_clave(palabras_clave):
    regex_palabra = r"^[a-zA-Z ]+$"
    palabrasLimpias = set()  # Utilizamos un conjunto para evitar duplicados

    umbral_similitud = 0.8

    for palabra in palabras_clave:
        if re.match(regex_palabra, palabra):
            # Verificar si una palabra similar ya está en el conjunto
            if not any(difflib.SequenceMatcher(None, palabra, p).ratio() > umbral_similitud for p in palabrasLimpias):
                palabrasLimpias.add(palabra)

    return list(palabrasLimpias)
