from googletrans import Translator
from utils.logger import log_request

translator = Translator()

def translate_text(text: str, lang: str) -> str:
    result = translator.translate(text, dest=lang)
    log_request(text, lang, result.text)
    return result.text

def translate_bulk(texts: list, lang: str) -> list:
    return [translate_text(text, lang) for text in texts]