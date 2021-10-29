import tweepy
import os

def check_id(account):
    """ツイッターアカウントのIDチェック

    Parameters
    ----------
    account : str
        アカウントID

    Returns
    -------
    str
        エラーメッセージ
    """
    if account == "":
        return "アカウント名が入力されていません"
    if account == "@":
        return "アカウントが存在しません"
    if account[0] == "@":
        account = account[1:]
    auth = tweepy.OAuthHandler(os.environ["T_key"], os.environ["T_keys"])
    auth.set_access_token(os.environ["T_token"], os.environ["T_tokens"])

    api = tweepy.API(auth)
    try:
        user = api.get_user(id=account)
    except:
        return "アカウントが存在しません"
    if user.protected == True:
        return "相手のアカウントが鍵アカになっています"
    else:
        return ""

if __name__ == "__main__":
    error = check_id("yuukamiya68")
    print(error)