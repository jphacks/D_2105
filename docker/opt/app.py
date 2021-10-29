from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import re, uuid, os, asyncio, traceback
import movie_create.movie_create as mc
from nlp import emotion_adapter
from nlp import check
from composer import get_tempo, create_music
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import asyncio

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

# ページ表示関係
@app.route('/')
def index():
    return render_template(
        "index.html",
    )

@app.route('/req', methods=['POST'])
def req():
    email1 = request.form.get('email1')
    email2 = request.form.get('email2')
    twitter_id = request.form.get('twitter_id')

    # メールアドレスのバリデーションを設定
    email_pattern = "^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$"

    # twitterアカウントの状態確認
    twitter_status = check.check_id(twitter_id)

    if re.fullmatch(email_pattern, email1) == None:
        flash("不正なメールアドレスです")
        return redirect(url_for('index'))
    elif re.fullmatch(email_pattern, email2) == None:
        flash("不正なメールアドレスです")
        return redirect(url_for('index'))
    elif email1 != email2:
        flash("メールアドレスが一致しません")
        return redirect(url_for('index'))
    elif (twitter_status != ""):
        # Twitterアカウントの存在確認
        flash(twitter_status)
        return redirect(url_for('index'))

    else:
        # uuidが被らなくなるまで再発行する
        id = uuid.uuid4().hex
        while os.path.isdir('./movie/' + id):
            id = uuid.uuid4().hex

        # uuidと同名のディレクトリを作成する
        os.mkdir('./movie/' + id)
        print(f"created uuid: {id}")

        # twitterのidを書いておく
        if (twitter_id[0] == "@"):
            twitter_id = twitter_id[1:]
        with open(f"./movie/{id}/twitter_id.txt", 'w') as f:
            f.write(twitter_id)

        # 非同期的に曲生成を開始する
        loop = asyncio.new_event_loop()
        loop.run_in_executor(None, create_manager, id, email1)
        

        return redirect(url_for('accept', id=id))

@app.route('/<id>/accept')
def accept(id):
    if os.path.isdir('./movie/' + id) == False:
        return redirect(url_for('index'))

    return render_template(
        "accept.html",
    )

@app.route('/<id>/preview')
def preview(id):
    if os.path.isdir('./movie/' + id) == False:
        return redirect(url_for('index'))

    twitter_id = ""
    with open(f"./movie/{id}/twitter_id.txt", 'r') as f:
        twitter_id = f.read()

    return render_template(
        "preview.html",
        id=id,
        twitter_id=twitter_id,
    )

@app.route('/<id>/download')
def download(id):
    if os.path.isdir('./movie/' + id) == False:
        return redirect(url_for('index'))

    return send_file('movie/' + id + '/happy_birthday.mp4', as_attachment=True)

@app.route('/error')
def error():
    return render_template(
        "error.html",
    )

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# ページ表示関係 ここまで

def create_manager(id, email1):
    """
    「Twitter探し〜曲出力〜動画出力〜メール送信」までを管理する関数

    Parameter
    ---------
    id : str
        個人識別用uuid
    email1 : str
        返信用メールアドレス
    """
    try:
        #related_list = ['cherry', 'dog', 'idol']
        related_list = ['sea','history','shopping']
        positive_param = 0.3 #デバッグ用
        bpm = get_tempo.get_bpm(related_list,positive_param)
        create_music.create_music(related_list, positive_param, id)
        mc.movie_create(id, bpm, related_list)
        send_email(email1, id)
    except Exception as e:
        app.logger.error(str(e))
        app.logger.error(traceback.format_exc())

def send_email(email1, id):
    from_address = os.environ["from_address"]
    password = os.environ["password"]
    email_server = os.environ["email_server"]
    email_port = os.environ["email_port"]

    subject = '【HABIFY】動画の生成が完了しました'
    body_text = f'<p>ダウンロードは<a href="https://habify.herokuapp.com/{id}/preview">こちら</a>から</p>'
    from_address = from_address
    to_address = email1

    # SMTPサーバに接続
    smtpobj = smtplib.SMTP(email_server, email_port)
    smtpobj.starttls()
    smtpobj.login(from_address, password)

    # メール作成
    msg = MIMEText(body_text, 'html')
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if __name__=='__main__':
    # 感情判定のセットアップ
    emotion_adapter.setup_model()
    port = os.getenv('PORT')
    debug = False
    if (port is not None):
        port = int(port)
    else:
        port = 5000
        debug = True
    app.run(host="0.0.0.0", port=port, debug=debug)
