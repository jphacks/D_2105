import csv
#import joblib
import re

#file
#import test
import twitter
import translate
import emotion

def get_APIs(api_file_name="../instance/API.csv"):
    """APIの辞書を作成する。

    Parameters
    ----------
    api_file_name : str, optional
        APIの情報が書かれたcsvファイル, by default "API.csv"

    Returns
    -------
    api_dict : dict
        api_dict[API_name]=key or ...
    """
    api_dict = {}
    with open(api_file_name, "r")as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            api_dict[row[0]]=row[1]
    return api_dict

def nlp_control(id_, twitter_id, twitter_get_num=900, key_num=3, api_file_name="API.csv"):
    api_dict = get_APIs(api_file_name)
    #tweet_list = twitter.get_tweet(twitter_get_num, twitter_id, api_dict["T_key"], api_dict["T_keys"], api_dict["T_token"], api_dict["T_tokens"])
    tweet_list = joblib.load("twitter_result")
    keywords = []
    emotions = []
    tmp_list = []
    for i in range(len(tweet_list)):
        tweet_list[i] = re.sub(r"@\w+\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"@\w+\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"http.*", "", tweet_list[i])
        #splitchar = r"[\n。？！\?!‼︎⁉︎]"
        #tmp_list.extend(re.split(splitchar, tweet_list[i]))
        tmp_list.extend(re.split(r"\n", tweet_list[i]))
    tweet_list = tmp_list.copy()
    #translations = translate.translate(tweet_list, api_dict["WL_key"], api_dict["WL_url"])
    #joblib.dump(tweet_list, "twitter_result2")
    #translations = joblib.load("translate_result")
    #print(translations)
    #print(tweet_list)
    #emotion = emotion.get_emotion(translations, api_dict["WN_key"], api_dict["WN_url"])
    return id_, keywords, emotions

if __name__ == "__main__":
    nlp_control(0, "")