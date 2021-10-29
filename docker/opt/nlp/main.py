import csv
import re
import os

#file
import twitter
import translate
import emotion
import keywords
import decide_keywords
import emotion_adapter
import name_check

def nlp_control(id_, twitter_id, twitter_get_num=300, twitter_get_chara_num=10000, key_num=3, no_api=0):
    """nlp全体の制御プログラム。返り値とは別に、ツイッターアイコンの画像ファイルを作成する。

    Parameters
    ----------
    id_ : int
        ユーザーID
    twitter_id : str
        twitterのID（@は不要）
    twitter_get_num : int, optional
        取得する最大ツイート数, by default 500
    twitter_get_chara_num : int, optional
        取得する最大ツイート文字数, by default 10000
    key_num : int, optional
        欲しいキーワード数, by default 3
    no_api : int
        もしもの時の、API使わず結果だけ返すやつ（値が1の時）

    Returns
    -------
    keyword_list : list[str]
        キーワードのリスト
    emotion : dict
        感情分析の結果（例：{'sadness': 0.510395, 'joy': 0.465514, 'fear': 0.087964, 'disgust': 0.129827, 'anger': 0.15183}）
    emotion_pn : float
        float 1に近い: ポジティブ 0に近い: ネガティブ
    error_flag : str
        エラー内容を表示（エラーでなければ""）
    """
    if no_api == 1:
        try:
            error_flag = ""
            tweet_list, description, error_flag = twitter.get_tweet(twitter_get_num, twitter_get_chara_num, twitter_id, os.environ["T_key"], os.environ["T_keys"], os.environ["T_token"], os.environ["T_tokens"])
            if error_flag != "":
                return [], {}, -1, error_flag
            translations = translate.translate(tweet_list, os.environ["WL_key"], os.environ["WL_url"])
            translations = "".join(translations)
            emotions = emotion.get_emotion(translations, os.environ["WN_key"], os.environ["WN_url"])
            description_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], [description])
            tweet_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], tweet_list)
            name_list = name_check.name_check(os.environ["G_id"], tweet_list)
            name_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], name_list)
            keyword_list = decide_keywords.decide_keywords(description_keywords, tweet_keywords, name_keywords, key_num, twitter_get_num)
            emotion_pn = emotion_adapter.tweets2posi_nega(tweet_list)
            return keyword_list, emotions, emotion_pn, ""
        except Exception as e:
            print(e)
            keyword_list_e = ['japnanese', 'gourmet', 'sea']
            emotions_e = {'sadness': 0.092843, 'joy': 0.706041, 'fear': 0.054193, 'disgust': 0.034763, 'anger': 0.103145}
            emotion_pn_e = 1.0
            return keyword_list_e, emotions_e, emotion_pn_e, ""
    else:
        error_flag = ""
        try:
            tweet_list, description, error_flag = twitter.get_tweet(twitter_get_num, twitter_get_chara_num, twitter_id, os.environ["T_key"], os.environ["T_keys"], os.environ["T_token"], os.environ["T_tokens"])
        except Exception as e:
            print(e)
            return [], {}, -1, "ツイートの取得に失敗しました"
        if error_flag != "":
            return [], {}, -1, error_flag
        try:
            translations = translate.translate(tweet_list, os.environ["WL_key"], os.environ["WL_url"])
            translations = "".join(translations)
            emotions = emotion.get_emotion(translations, os.environ["WN_key"], os.environ["WN_url"])
            description_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], [description])
            tweet_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], tweet_list)
            name_list = name_check.name_check(os.environ["G_id"], tweet_list)
            name_keywords = keywords.get_keywords(os.environ["DB_user"], os.environ["DB_pass"], os.environ["DB_name"], name_list)
            keyword_list = decide_keywords.decide_keywords(description_keywords, tweet_keywords, name_keywords, key_num, twitter_get_num)
            emotion_pn = emotion_adapter.tweets2posi_nega(tweet_list)
            return keyword_list, emotions, emotion_pn, ""
        except Exception as e:
            print(e)
            return [], {}, -1, "処理でエラーが生じました"

if __name__ == "__main__":
    keyword_list, emotions, emotion_pn, error_message = nlp_control(0, "jphacks2021")
    print(keyword_list)
    print(emotions)
    print(emotion_pn)
    if error_message != "":
        print(error_message)