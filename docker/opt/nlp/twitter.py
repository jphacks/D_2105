import re
import tweepy
#import joblib
import math

UNIT_NUM = 10

def get_tweet(min_num, account, api_key, api_key_secret, access_token, access_token_secret):
    """対象のツイートを取得

    Parameters
    ----------
    min_num : int
        最低限欲しいツイート数
    account : str
        アカウントID
    api_key : str
    api_secret : str
    access_token : str
    access_token_secret : str

    Returns
    -------
    tweet_list : list[str]
        ツイートのリスト
    """
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    tweet_list = []
    paging_num = math.ceil(min_num/UNIT_NUM)
    for page in range(paging_num):
        statuses = api.user_timeline(id=account, count=UNIT_NUM, page=page, include_rts=False)
        for status in statuses:
            tweet_list.append(status.text)
    tmp_list = []
    for i in range(len(tweet_list)):
        tweet_list[i] = re.sub(r"@\w+\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"@\w+\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"http.*", "", tweet_list[i])
        tmp_list.extend(re.split(r"\n", tweet_list[i]))
    tweet_list = tmp_list.copy()
    
    return tweet_list

def main():
    tweet_list = get_tweet()
    #[print(tweet) for tweet in tweet_list]
    #print(len(tweet_list))
    return

if __name__ == "__main__":
    main()