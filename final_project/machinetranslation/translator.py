"""
Week 2
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
text_to_translate = 'Hello, World'

# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    englishToFrench
    """
    #write the code here
    if englishText == "":
        return ""
    model_id = 'en-fr'
    translation = language_translator.translate(
    text=englishText,
    model_id=model_id).get_result()
    a = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
    return a["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    """
    vice versa
    """
    #write the code here
    if frenchText == "":
        return ""
    model_id = 'fr-en'
    translation = language_translator.translate(
    text=frenchText,
    model_id=model_id).get_result()
    a = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
    return a["translations"][0]["translation"]

print("1. " + englishToFrench(""))
print("2. " + frenchToEnglish(""))
# # Translate
# translation = language_translator.translate(
#     text=text_to_translate,
#     model_id=model_id).get_result()

# # Print results
# print(json.dumps(translation, indent=2, ensure_ascii=False))
