import csv
import joblib
import re
import os

#file
#import test
import twitter
import translate
import emotion
import keywords
import decide_keywords

def nlp_control(id_, twitter_id, twitter_get_num=900, key_num=3):
    """nlp全体の制御プログラム。返り値とは別に、ツイッターアイコンの画像ファイルを作成する。

    Parameters
    ----------
    id_ : int
        ユーザーID
    twitter_id : str
        twitterのID（@は不要）
    twitter_get_num : int, optional
        取得したいツイート数, by default 900
    key_num : int, optional
        欲しいキーワード数, by default 3

    Returns
    -------
    keyword_list : list[str]
        キーワードのリスト
    emotion : dict
        感情分析の結果（例：{'sadness': 0.510395, 'joy': 0.465514, 'fear': 0.087964, 'disgust': 0.129827, 'anger': 0.15183}）
    error_flag : str
        エラー内容を表示（エラーでなければ""）
    """
    if twitter_id == "":
        return [], {}, "アカウント名が入力されていません"
    tweet_list, description, error_flag = twitter.get_tweet(twitter_get_num, twitter_id, os.environ["T_key"], os.environ["T_keys"], os.environ["T_token"], os.environ["T_tokens"])
    #tweet_list = joblib.load("twitter_result")
    #error_flag = 0
    #description = "ピアノ弾きます DTMやります 演奏&作曲で動画上げてます良ければお聴きくださいAAR(Anti-AgingRecord)所属 https://m.youtube.com/c/sawapypiano PythonとC++で色々やってるLinux使い"
    #joblib.dump(tweet_list, "twitter_result")
    if error_flag != "":
        return [], {}, error_flag
    translations = translate.translate(tweet_list, os.environ["WL_key"], os.environ["WL_url"])
    #translations = joblib.load("translation_result")
    #joblib.dump(translations, "translation_result")
    translations = "".join(translations)
    emotions = emotion.get_emotion(translations, os.environ["WN_key"], os.environ["WN_url"])
    #emotions = joblib.load("emotion_result")
    #joblib.dump(emotions, "emotion_result")
    description_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], [description])
    joblib.dump(description_keywords, "description_keywords")
    tweet_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], tweet_list)
    joblib.dump(tweet_keywords, "tweet_keywords")
    keyword_list = decide_keywords.decide_keywords(description_keywords, tweet_keywords, key_num, twitter_get_num)
    joblib.dump(keyword_list, "keyword_result")
    
    print(keyword_list)
    print(emotions)
    return keyword_list, emotions, ""

if __name__ == "__main__":
    nlp_control(0, "jphacks2021")