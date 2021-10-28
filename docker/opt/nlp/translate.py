from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import time
#import joblib

VERSION = '2018-05-01'
#翻訳したい文章は1文ごとのリストにする

def change_to_d2list(text_list):
    return_list = []
    tmp_list = []
    byte = 0
    for text in text_list:
        byte += len(text.encode())
        if byte >= 45000:
            return_list.append(tmp_list)
            tmp_list = []
            byte = 0
        tmp_list.append(text)
    if tmp_list != []:
        return_list.append(tmp_list)
    return return_list

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
    text_list = change_to_d2list(text)
    #翻訳する
    translations = []
    for text in text_list:
        authenticator = IAMAuthenticator(api_key)
        language_translator = LanguageTranslatorV3(
            version=VERSION,
            authenticator=authenticator
        )
        language_translator.set_service_url(url)
        #APIの入力をWatsonの学習データに渡さないようにするオプション
        language_translator.set_default_headers({'x-watson-learning-opt-out': "true"})
        translation = language_translator.translate(text=text, model_id="ja-en")
        #print(translation)
        #print(translation.get_result())
        #joblib.dump(translation, "translation_result")
        translation = translation.get_result()["translations"]
        for tr in translation:
            translations.append(tr["translation"])
    return translations

def main():
    translate(TEXT, API_KEY, URL)
if __name__ == "__main__":
    main()