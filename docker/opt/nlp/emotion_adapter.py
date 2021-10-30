"""
バンダイナムコ研究所 提供 感情判定Adapters
"""
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdapterType
from numpy import average
import pickle as pick

MODEL_DIR = "./nlp/"
def setup_model():
    """
    起動時に一度だけ実行される
    提供されているモデルをDLしてpickleオブジェクトに保存する
    """
    model = AutoModelForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
    tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
    
    with open(MODEL_DIR + 'model.pickle', 'wb') as f:
        pick.dump(model, f)
    with open(MODEL_DIR + 'tokenizer.pickle', 'wb') as f:
        pick.dump(tokenizer, f)

def load_model():
    """
    保存した提供されているモデルを読み込む

    Returns
    ----------
    model
        提供されたmodel
    tokernizre
        提供されたヤツ(よくわかってない)
    """
    with open(MODEL_DIR + 'model.pickle', 'rb') as f:
        model = pick.load(f)
    with open(MODEL_DIR + 'tokenizer.pickle', 'rb') as f:
        tokenizer = pick.load(f)
    return model, tokenizer

def tweets2posi_nega(tweets):
    """
    ツイートのリストからポジティブ/ネガティブの判定をする.
    全ツイートの平均を返す0から1で返す. 1に近いほどポジティブ.

    Parameters
    ----------
    tweets : [String]
        ツイート内容のリスト

    Return
    ----------
    float
        1に近い: ポジティブ
        0に近い: ネガティブ
    """
    # 保存したモデルの読み込み
    model, tokenizer = load_model()

    results = []
    for tweet in tweets:
        if tweet == "":
            continue
        token_ids = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(tweet))
        input_tensor = torch.tensor([token_ids])
        outputs = model(input_tensor, adapter_names=['sst-2'])
        result = torch.argmax(outputs[0]).item()
        results.append(result)
        # print(f"{result}: {tweet}") # 確認用
    del model
    del tokenizer
    return average(results)

def predict(sentence, tokenizer, model):
    """
    1つの文章のポジティブ/ネガティブを判定する.
    
    Parameters
    ----------
    sentence : String
        解析したい文章
    tokenizer : transformers.models.bert.modeling_bert.BertForSequenceClassification
    model : transformers.models.bert_japanese.tokenization_bert_japanese.BertJapaneseTokenizer

    Return
    ----------
    int : 判定結果
        1: ポジティブ
        0: ネガティブ
    """
    
    token_ids = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(sentence))
    input_tensor = torch.tensor([token_ids])
    outputs = model(input_tensor, adapter_names=['sst-2'])
    result = torch.argmax(outputs[0]).item()

    return result

if __name__ == "__main__":
    
    # setup_model()

    # テスト用
    print(tweets2posi_nega([
        "ウチらズッ友だョ",
        "楽しい",
        "全然面白くない",
        "うち（ユニット）のクロスフェード上げられるの、M3前日の夜じゃないかな😇",
        "こんなえげつない大学進学率で大学の無償化なんい無意味だべ",
        "わーん、素敵…！",
        "春のM3はね…行きたいわね…",
        "M3を乗り切る体力があるのか心配だぞ……。",
    ]))
