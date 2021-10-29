# HABIFY 〜オンリーワンな Happy Birthday to You をお届けします〜

[![HABIFY Logo](https://github.com/jphacks/D_2105/blob/master/docker/opt/static/img/logo.png?raw=true)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
HABIFY 〜オンリーワンな Happy Birthday to You をお届けします〜
### 背景(製品開発のきっかけ、課題等)
- コロナ禍で弱まってしまった友人や家族とのつながりを再び深めたい
- 年に一度の誕生日に新しい祝い方を提案したい
- 日本全国誰に対しても同じバースデーソングはつまらない

このような課題を解決したいという思いと, 
- メンバー全員の音楽のスキルを活かしたものを作りたい
- メンバー全員がPythonの関係者(?)なので, スキルアップや実践経験を積みたい

このようなチームメンバーの思いから, 特別なバースデーソングによる新たな誕生日の祝い方を提案します.

### 製品説明（具体的な製品の説明）
Twitterの投稿を元にその人の趣味趣向や性格を分析し, その人のためのHappy Birthday to You のアレンジを生成します.

使い方は簡単. http://habify.herokuapp.com にアクセスして, あなたのメールアドレスと, 誕生日を祝いたい相手のTwitterのIDを入力して開始ボタンを押すだけ!!
曲が完成したら, メールに
- 動画の再生
- Twitterでのシェア
- ダウンロード  

をできるページのURLが送信されます.
あとはページ上からTwitterで送るも良し, 動画をダウンロードして他のツールで送るも良し.
盛大にお祝いしてください.

### 特長
1. 生成される曲のパターンは64bit(2^64≒1.8x19^19)通り以上! その中から, アナタが祝いたい相手に最適なHappyBirthdayToYouをお届けします.
1. ロゴやアイコンなどの画像素材は全てチーム内のデザイナーが作成しました. 
1. DockerとGitHubActionsを用いたことで, 快適な開発環境とデプロイを実現しました.

### 解決出来ること
1. コロナ禍で失われてしまった, 人との交流を再開するきっかけとなる.
1. 面と向かって「誕生日おめでとう」と言いにくい時や相手に対してお祝いを伝える手段となる.

### 今後の展望
1. 曲調をより多彩な特徴に対応させる.
1. イントロやアウトロも生成できるようにする.
1. 動画生成の間などでの広告収入を追加する.
1. SNSでの拡散を狙う(特に, 講義のオンライン化で友人との交流が減った大学生を対象にする).

### 注力したこと（こだわり等）
* 祝いたい相手に合わせた曲を生成するための自然言語処理や編曲の独自の組み合わせやロジックを開発したこと.
* 人名抽出を使ってキーワードの単語の誤抽出を防いだ.
* 単語のイメージと乖離しないように, 楽器からリズムまで, 曲の全ての構成要素を検討したこと.
* 音楽理論の上で破綻しておらず, 不自然にならないコード進行を生成できるようにしたこと.
* 静止画とBPMからテンポに合わせて動く動画を生成したこと.

## 開発技術
### 活用した技術
* 開発環境: Docker
* 使用言語: python3.9
* デプロイ先: Heroku
* デプロイ管理: GitHubActions
* mongoDB
* OpenCV
* [gunicorn](https://gunicorn.org)

#### API・データ
* [Twitter API](https://developer.twitter.com/en/products/twitter-api/)
* [バンダイナムコ研究所 感情判定Adapters](https://github.com/BandaiNamcoResearchInc/sentiment-analysis-adapter)
* [NTTレゾナント gooラボAPI（固有表現抽出API）](https://labs.goo.ne.jp/api/jp/named-entity-extraction/)
* [IBM Watson Language Translator](https://www.ibm.com/jp-ja/cloud/watson-language-translator/)
* [IBM Watson Natural Language Understanding](https://www.ibm.com/cloud/watson-natural-language-understanding/)
* [MongoDB Cloud](https://www.mongodb.com/ja-jp/cloud)


#### フレームワーク・ライブラリ・モジュール(主要なものを抜粋)
* flask
* pretty_midi(MIDIデータ加工)
* librosa(音声ファイル入出力)
* midi2audio(音声出力)
* moviepy(動画出力)
* OpenCV

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。
* 伴奏のコード進行の生成
* キーワードとなる単語リスト
