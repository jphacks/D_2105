# コンテナのビルドから使うまで(初回起動時&構成を変更した時のみ)
```
$ docker-compose up -d --build
$ docker-compose exec python3 bash
```

# コンテナを使うとき(2回目以降)
```
$ docker-compose start
$ docker-compose exec python3 bash
```

# flaskサーバーの起動
```
$ docker-compose start
$ docker-compose exec python3 bash
```
の後で
```
root@xxxxxxxxxxx:~# cd opt
root@xxxxxxxxxxx:~# python app.py
```

止める時は, Ctrl+C→exit

# 作業を終わってdockerを止めたいとき
```
root@xxxxxxxxxx ディレクトリ名# exit
$ docker-compose stop
```

# 追加のPythonモジュールが必要なとき
1. まずコンテナに入って`pip install モジュール名`
1. 成功したら, Dockerfileの最終行(たぶん)`RUN pip install 〜〜〜〜`にモジュール名を追記
1. __コンテナのビルドから使うまで__ を実行
1. 成功したら, 全員にDockerfileを更新した旨を連絡. 全員 __コンテナのビルドから使うまで__ を実行
