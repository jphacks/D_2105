import re
import tweepy
#import joblib
import math
import urllib.request
import urllib.error

UNIT_NUM = 100

def download_image(url, icon_size=200, dst_path="icon.png"):
    """URLから画像をダウンロードする

    Parameters
    ----------
    url : str
        画像のURL
    icon_size : int
        画像サイズ(24, 48, 73, 200, 400, 512のいずれか), by default 200
    dst_path : str, optional
        画像の保存場所, by default "icon.png"
    """
    url = url.replace("_normal.jpg", "_"+str(icon_size)+"x"+str(icon_size)+".jpg")
    print(url)
    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

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
    description : str
        プロフィールの文
    error_flag : int
        1ならエラー、0ならOK
    """
    if account[0] == "@":
        account = account[1:]
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    try:
        user = api.get_user(id=account)
    except:
        return [], "", 1
    if user.protected == True:
        return [], "", 1
    description = user.description
    img_url = user.profile_image_url_https
    download_image(img_url)
    
    tweet_list = []
    paging_num = math.ceil(min_num/UNIT_NUM)
    for page in range(paging_num):
        statuses = api.user_timeline(id=account, count=UNIT_NUM, page=page, include_rts=False)
        for status in statuses:
            tweet_list.append(status.text)
    for i in range(len(tweet_list)):
        tweet_list[i] = re.sub(r"@\w+\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"http.*", "", tweet_list[i])
    
    return tweet_list, description, 0

def main():
    tweet_list = get_tweet()
    #[print(tweet) for tweet in tweet_list]
    #print(len(tweet_list))
    return

if __name__ == "__main__":
    main()