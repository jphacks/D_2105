from requests_oauthlib import OAuth1Session
import os
from instance import api_key
import time
# ツイート用エンドポイント
twUrl = "https://api.twitter.com/1.1/statuses/update.json"
# メディア用エンドポイント
upUrl = "https://upload.twitter.com/1.1/media/upload.json"


def upload(id="1"):
    # ファイル名
    file_name = f"movie/{id}/happy_birthday.mp4"
    # 認証
    twitter = OAuth1Session(os.environ["T_key"], os.environ["T_keys"], os.environ["T_token"], os.environ["T_tokens"])
    # サイズ指定が必要なので後で使う
    totalBytes = os.path.getsize(file_name)

    # ID取得
    initParams = {
        "command": "INIT",
        "media_type": "video/mp4",
        "total_bytes": totalBytes,
        "media_category": "tweet_video"
    }
    initResponse = twitter.post(url=upUrl, data=initParams)
    mediaId = initResponse.json()['media_id']

    # 分割アップロード処理
    segmentId = 0
    bytesSent = 0
    with open(file_name, "rb") as f: #ByteIO型はgetsize含めて別に作りこみが必要
        while bytesSent < totalBytes:
            chunk = f.read(1*1024*1024)

            addParams = {
                "command": "APPEND",
                "media_id": mediaId,
                "segment_index": segmentId
            }

            files = {
                "media": chunk
            }

            appendResponse = twitter.post(url=upUrl, data=addParams, files=files)
            print(appendResponse)

            segmentId = segmentId + 1
            bytesSent = f.tell() # バイナリモードの時にファイルの先頭からのバイト数を返却する
            print("%s of %s bytes uploaded" % (str(bytesSent), str(totalBytes)))

        print("upload complete")

        # ファイナライズ処理
        finalizeParams = {
            "command": "FINALIZE",
            "media_id": mediaId
        }

        finalizeResponse = twitter.post(url=upUrl, data=finalizeParams)

        statusParams = {
            "command": "STATUS",
            "media_id": mediaId
        }

        statusResponse = twitter.get(url=upUrl, params=statusParams)
        print(statusResponse)
        processingInfo = statusResponse.json().get("processing_info", None)

        while processingInfo['state'] == 'in_progress':
            time.sleep(1)
            statusResponse = twitter.get(url=upUrl, params=statusParams)
            processingInfo = statusResponse.json().get("processing_info", None)
            print(processingInfo)

        # ツイートする
        params = {
            "status": "動画ツイート",
            "media_ids": mediaId
        }
        twitter.post(url=twUrl, data=params)
if __name__ == "__main__":
    upload()