import csv
#import joblib
import re
import os

#file
#import test
import twitter
import translate
import emotion
import keywords

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
    error_flag : int
        1ならエラー、0ならOK
    """
    tweet_list, description, error_flag = twitter.get_tweet(twitter_get_num, twitter_id, os.environ["T_key"], os.environ["T_keys"], os.environ["T_token"], os.environ["T_tokens"])
    if error_flag == 1:
        return [], {}, 1
    #tweet_list = joblib.load("twitter_result")
    translations = translate.translate(tweet_list, os.environ["WL_key"], os.environ["WL_url"])
    #joblib.dump(tweet_list, "twitter_result2")
    #translations = joblib.load("translate_result")
    #print(translations)
    #print(tweet_list)
    emotions = emotion.get_emotion(translations, os.environ["WN_key"], os.environ["WN_url"])
    keyword_list = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], tweet_list, key_num)
    return keyword_list, emotions, 0

if __name__ == "__main__":
    nlp_control(0, "")