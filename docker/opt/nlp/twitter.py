import re
import tweepy
#import joblib
import math
import urllib.request
import urllib.error

UNIT_NUM = 50

def download_image(id_, url, icon_size=200, dst_path="./movie/"):
    """URLから画像をダウンロードする

    Parameters
    ----------
    id_ : int
        受付ID
    url : str
        画像のURL
    icon_size : int
        画像サイズ(24, 48, 73, 200, 400, 512のいずれか), by default 200
    dst_path : str, optional
        画像の保存場所, by default "icon.png"
    """
    url = url.replace("_normal.jpg", "_"+str(icon_size)+"x"+str(icon_size)+".jpg")
    data = urllib.request.urlopen(url).read()
    with open(dst_path+str(id_)+"/icon.png", mode="wb") as f:
        f.write(data)

def get_tweet(id_, max_num, max_chara_num, account, api_key, api_key_secret, access_token, access_token_secret):
    """対象のツイートを取得

    Parameters
    ----------
    id_ : int
        受付ID
    max_num : int
        ツイート数の上限
    max_chara_num : int
        ツイート文字数の上限
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
    error_flag : str
        エラー内容を表示（エラーでなければ""）
    """
    if account == "@":
        return [], "", "アカウントが存在しません"
    if account[0] == "@":
        account = account[1:]
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    try:
        user = api.get_user(id=account)
    except:
        return [], "", "アカウントが存在しません"
    if user.protected == True:
        return [], "", "相手のアカウントが鍵アカになっています"
    description = user.description
    img_url = user.profile_image_url_https
    download_image(id_, img_url)
    chara_count = 0
    tweet_list = []
    paging_num = math.ceil(max_num/UNIT_NUM)
    for page in range(paging_num):
        statuses = api.user_timeline(id=account, count=UNIT_NUM, page=page, include_rts=True)
        for status in statuses:
            tweet_text = status.text
            chara_count += len(tweet_text)
            tweet_list.append(tweet_text)
        if chara_count >= max_chara_num:
            break

    for i in range(len(tweet_list)):
        tweet_list[i] = re.sub(r"@\w+\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"\s", "", tweet_list[i])
        tweet_list[i] = re.sub(r"http.*", "", tweet_list[i])
    return tweet_list, description, ""

def main():
    tweet_list = get_tweet()
    #[print(tweet) for tweet in tweet_list]
    #print(len(tweet_list))
    return

if __name__ == "__main__":
    main()