# HABIFY 〜オンリーワンな Happy Birthday to You をお届けします〜

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2021/07/JPHACKS2021_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
HABIFY 〜オンリーワンな Happy Birthday to You をお届けします〜
### 背景(製品開発のきっかけ、課題等）
- コロナ禍で弱まってしまった友人や家族とのつながりを再び深めたい
- 年に一度の誕生日に新しい祝い方を提案したい
- メンバー全員の音楽のスキルを活かしたものを作りたい
- メンバー全員がPythonの関係者(?)なので, スキルアップや実践経験を積みたい
- 日本全国誰に対しても同じバースデーソングはつまらない

...このような思いから, 特別なバースデーソングによる新たな誕生日の祝い方を提案する.

### 製品説明（具体的な製品の説明）
Twitterの投稿を元にその人の趣味趣向や性格を分析し, その人のためのHappy Birthday to You のアレンジを生成する.



### 特長
####1. 特長1
####2. 特長2
####3. 特長3

### 解決出来ること
### 今後の展望
### 注力したこと（こだわり等）
* 画像素材は全て自前で用意(デザイナー担当に感謝)
* 出力される曲のバリエーションは100万通り以上(たぶん1億超えてるんじゃないかな)(多すぎて数えるの諦めた)

## 開発技術
### 活用した技術
* 開発環境: docker
* 使用言語: python3.9
* デプロイ先: Heroku
* mongoDB

#### API・データ
* [Twitter API](https://developer.twitter.com/en/products/twitter-api/)
* [gooラボAPI（固有表現抽出API）](https://labs.goo.ne.jp/api/jp/named-entity-extraction/)
* [IBM Watson Language Translator](https://www.ibm.com/jp-ja/cloud/watson-language-translator/)
* [IBM Watson Natural Language Understanding](https://www.ibm.com/cloud/watson-natural-language-understanding/)
* [MongoDB Cloud](https://www.mongodb.com/ja-jp/cloud)


#### フレームワーク・ライブラリ・モジュール(主要なものを抜粋)
* flask
* pretty_midi(MIDIデータ加工)
* librosa(音声読み込み)
* midi2audio(音声出力)
* moviepy(動画出力)

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
* 
