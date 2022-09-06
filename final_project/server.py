from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    a = translator.englishToFrench(textToTranslate)
    print(a)
    return a #"Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    a = translator.frenchToEnglish(textToTranslate)
    print(a)
    return a #"Translated text to English"

@app.route("/index.html")
def renderIndexPage():
    # Write the code to render template
    return
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
