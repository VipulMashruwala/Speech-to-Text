from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import smtplib

apikey_s2t="yG0vCCZZ_CdThOe1e8itdCAeBtNUlP47Tuy0AS2L5QnE"
url_s2t="https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/e7afb707-9894-4c4d-83ad-076c441c9783"

apikey_lt="5jlLqVQZwj4VS6Yg8gAkW2A80_PbHbY7kjb2QxUU7-pK"
url_lt="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/05655017-225d-4dce-9198-9fd5694eecb1"
version="2018-05-01"

authenticator=IAMAuthenticator(apikey_s2t)
s2t=SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)

authenticator=IAMAuthenticator(apikey_lt)
translator=LanguageTranslatorV3(version=version,authenticator=authenticator)
translator.set_service_url(url_lt)

with open("PolynomialRegressionandPipelines.mp3",mode="rb") as wav:
    recognize_text=s2t.recognize(audio=wav,content_type="audio/mp3")

    dict=recognize_text.result

    input_text = []
    for i in dict["results"]:
        get_text = i["alternatives"][0]["transcript"]
        input_text.append(get_text)

    final_data=[]
    for i in input_text:
        translation_response=translator.translate(text=i,model_id="en-hi")
        get_translation=translation_response.get_result()
        hindi_translation=get_translation["translations"][0]["translation"]
        final_data.append(hindi_translation)





