import nltk
import spacy
import obtener_contenido_wikipedia
import limpiar_palabras
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def extraer_sustantivos_spacy(texto):
    # Cargar el modelo en español
    nlp = spacy.load("es_core_news_sm")

    # Procesar el texto con spaCy
    doc = nlp(texto)

    # Extraer sustantivos
    sustantivos = [token.text for token in doc if token.pos_ == "NOUN"]

    return sustantivos

def buscar_sustantivos(tema):
    # Obtener el contenido de Wikipedia para el tema proporcionado
    texto = obtener_contenido_wikipedia.obtener_contenido_wikipedia(tema)

    # Dividir el texto en oraciones
    oraciones = nltk.sent_tokenize(texto)

    sustantivos = []

    # Procesar cada oración y extraer sustantivos utilizando spaCy
    for oracion in oraciones:
        sustantivos += extraer_sustantivos_spacy(oracion)

    # Limpiar las palabras clave
    sustantivos = limpiar_palabras.limpiar_palabras_clave(sustantivos)

    return sustantivos
