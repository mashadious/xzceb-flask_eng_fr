'''
This is a code to enable a translation from english to french and vice versa
'''
import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

VERSION='2018-05-01'
AUTHENTICATOR = IAMAuthenticator(APIKEY)

language_translator = LanguageTranslatorV3(version=VERSION,authenticator=AUTHENTICATOR)
language_translator.set_service_url(URL)


def english_to_french(english_text):
    '''
    Translate Text from English to French
    '''
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation= translation_response.get_result()
    french_text= translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    '''
    Translate Test from French to English
    '''
    translation_response = language_translator.translate(text=french_text, model_id='fr-en')
    translation= translation_response.get_result()
    english_text= translation['translations'][0]['translation']
    return english_text
