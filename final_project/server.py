from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext= translator.english_to_french(textToTranslate)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishtext= translator.french_to_english(textToTranslate)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # rendering Index page
    Return render_template(‘index.html’)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
