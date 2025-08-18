# utils/translator.py
from deep_translator import GoogleTranslator
from langdetect import detect

def detect_language(text: str) -> str:
    if not text.strip():
        print("⚠️ Empty input for language detection. Defaulting to English.")
        return "en"
    try:
        return detect(text)
    except LangDetectException as e:
        print(f"⚠️ Language detection failed: {e}. Defaulting to English.")
        return "en"




def translate_to_english(text: str) -> str:
    """Translate from any language to English"""
    return GoogleTranslator(source='auto', target='en').translate(text)

def translate_from_english(text: str, target_lang: str) -> str:
    """Translate English to target language"""
    return GoogleTranslator(source='en', target=target_lang).translate(text)
