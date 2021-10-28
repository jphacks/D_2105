"""
バンダイナムコ研究所 提供 感情判定Adapters
"""
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdapterType
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
    model = AutoModelForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
    tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")


    pass

def predict(sentence, tokenizer, model):
    """
    1つの文章のポジティブ/ネガティブを判定する.
    
    """
    token_ids = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(sentence))
    input_tensor = torch.tensor([token_ids])
    outputs = model(input_tensor, adapter_names=['sst-2'])
    result = torch.argmax(outputs[0]).item()

    return result