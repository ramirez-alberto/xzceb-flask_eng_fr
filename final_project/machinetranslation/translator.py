'''
    This module use IBM Watson Language Translation services to
    parse strings from english to french and vice versa.
'''
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

#   Make a instance of IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

try:
    #   Custom code
    def english_to_french(english_text):
        '''
            Translate from English to French
        '''
        if english_text is not None:
            response = language_translator.translate(
                text=english_text ,
                model_id='en-fr').get_result()
            french_text = response['translations'][0]['translation']
        else:
            french_text = "Null value passed"
        return french_text

    def french_to_english(french_text):
        '''
            Translate from French to English
        '''
        if french_text is not None:
            response = language_translator.translate(
                text=french_text ,
                model_id='fr-en').get_result()
            english_text = response['translations'][0]['translation']
        else:
            english_text = "Null value passed"
        return english_text

except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)



"""Example:
translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))
"""