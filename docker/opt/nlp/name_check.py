from goolabs import GoolabsAPI
import time

def name_check(api_id, text_list):
    """固有表現抽出器で名前と判断された語のリストを取得

    Parameters
    ----------
    api_id : str

    text_list : list[str]
        ツイッターの文章のリスト

    Returns
    -------
    name_list : list[str]
        名前と判断された語（重複あり）
    """
    n_list = ["鬼太郎", "ぬらりひょん", "コナン", "金田一", "モリアーティー", "ホームズ",
              "水谷隼", "張本智和", "石川佳純", "丹羽孝希", "陳夢", "馬龍", "伊藤美誠", "宇田幸矢", "許キン"]
    name_list = []
    api = GoolabsAPI(api_id)
    for i in range(int(len(text_list)/100)+1):
        if i != int(len(text_list)/100):
            text = "".join(text_list[i*100:(i+1)*100])
        elif len(text_list)%100 != 0:
            text = "".join(text_list[i*100:])
        ne_list = api.entity(sentence=text, class_filter="PSN")["ne_list"]
        for name in ne_list:
            if name[0] not in n_list:
                name_list.append(name[0])
        time.sleep(1)
    return name_list

def main():
    tweet_list = joblib.load("twitter_result2")
    name_check("", tweet_list)
    return

if __name__ == "__main__":
    main()