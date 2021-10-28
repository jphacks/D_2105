from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#import joblib

VERSION = '2018-05-01'
#翻訳したい文章は1文ごとのリストにする

def translate(text, api_key, url):
    """WatsonAPIを使って日本語を英語に翻訳する

    Parameters
    ----------
    text : list[str]
        一文ごとに区切られた、翻訳したい文章
    api_key : str
    url : str

    Returns
    -------
    translations : dict
        APIから返ってきた結果
    """
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version=VERSION,
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    #APIの入力をWatsonの学習データに渡さないようにするオプション
    language_translator.set_default_headers({'x-watson-learning-opt-out': "true"})
    #翻訳する
    translation = language_translator.translate(text=text, model_id="ja-en")
    #print(translation)
    #print(translation.get_result())
    #joblib.dump(translation, "translation_result")
    translation = translation.get_result()["translations"]
    translations = [text["translation"] for text in translation]
    return translations

def main():
    translate(TEXT, API_KEY, URL)
if __name__ == "__main__":
    main()