def decide_keywords(description_keywords, tweet_keywords, name_keywords, keyword_num, tweet_len):
    """プロフィールとツイートに出てきたキーワード数を組み合わせて出力

    Parameters
    ----------
    description_keywords : dict
        プロフィールのキーワード数
    tweet_keywords : dict
        ツイートのキーワード数
    tweet_keywords : dict
        人名抽出からのキーワード数
    keyword_num : int
        出力したいキーワード数
    tweet_len : int
        ツイート数

    Returns
    -------
    keyword_list : list[str]
        キーワードのリスト
    """
    sum_ = sum(tweet_keywords.values())
    weight = int(tweet_len/100)*3
    keyword_count = {}
    keyword_list = []
    for key in description_keywords.keys():
        keyword_count[key] = description_keywords[key]*weight+tweet_keywords[key]-name_keywords[key]
    for i in range(keyword_num):
        max_k = max(keyword_count, key=keyword_count.get)
        keyword_list.append(max_k)
        keyword_count[max_k] = 0
    return keyword_list

if __name__ == "__main__":
    decide_keywords()