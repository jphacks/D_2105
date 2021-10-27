import pymongo
#import joblib

def get_keywords(user_name, password, db_name, text_list, keyword_num):
    """キーワードを取得する

    Parameters
    ----------
    user_name : str
        dbのユーザーネーム
    password : str
        dbのパスワード
    db_name : str
        dbの名前
    text_list : list[str]
        テキストのリスト
    keyword_num : int
        返すキーワードの数

    Returns
    -------
    keyword_list : list[str]
        キーワードのリスト
    """
    connection_url = "mongodb+srv://"+user_name+":"+password+"@cluster0.43xkd.mongodb.net/"+db_name+"?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client.keyword_db
    collection = db.keyword_collection
    find = collection.find()
    keyword_count = {}
    tmp_list = text_list.copy()
    prev = ""
    for doc in find:
        word = doc["word"]
        if word == "":
            continue
        keyword = doc["keyword"]
        if prev != keyword:
            text_list = tmp_list.copy()
        prev = keyword
        if keyword not in keyword_count.keys():
            keyword_count[keyword] = 0
        for i in range(len(text_list)):
            if word in text_list[i]:
                keyword_count[keyword] += 1
            text_list[i] = text_list[i].replace(word, "")
    keyword_list = []
    for i in range(keyword_num):
        max_k = max(keyword_count, key=keyword_count.get)
        keyword_list.append(max_k)
        keyword_count[max_k] = 0

    return keyword_list


if __name__ == "__main__":
    #tweet_list = joblib.load("twitter_result2")
    get_keywords()