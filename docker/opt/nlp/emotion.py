from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
#import joblib

VERSION = "2021-08-01"

def get_emotion(text, api_key, url):
    """入力されたテキスト(英語)の感情分析

    Parameters
    ----------
    text : str
        分析対象の文章
    api_key : str
    url : str

    Returns
    -------
    dict
        感情分析の結果
    """
    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version=VERSION,
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(url)
    #Watsonが入力データを使わないようにする
    natural_language_understanding.set_default_headers({'x-watson-learning-opt-out': "true"})

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions()))
    #joblib.dump(response, "emotion_result")
    return response

def main():
    get_emotion()
if __name__ == "__main__":
    main()
