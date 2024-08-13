from googletrans import Translator
import sys

translator = Translator(service_urls=['translate.google.com.tr'])

def translate(inputText):
    languages = ["tr", "en", "de", "es", "fr", "ca", "ro"]
    riverLanguages = ["trTR", "enEN", "deDE", "esES", "frFR", "caCA", "roRO"]
    textLang = translator.detect(inputText).lang
    print('language: [')
    for language in languages:
        if language == textLang:
            continue
        print('{\n"Code": "' + riverLanguages[languages.index(language)] + '",\n"Label": "'+ translator.translate(inputText, dest=language).text +'"\n}')
    print(']')
    
inputText = sys.argv[1]
translate(inputText)