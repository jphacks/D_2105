from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import re, uuid, os, asyncio, traceback
import movie_create.movie_create as mc

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

    if re.fullmatch(email_pattern, email1) == None:
        flash("不正なメールアドレスです")
        return redirect(url_for('index'))
    elif re.fullmatch(email_pattern, email2) == None:
        flash("不正なメールアドレスです")
        return redirect(url_for('index'))
    elif email1 != email2:
        flash("メールアドレスが一致しません")
        return redirect(url_for('index'))
    else:
        # uuidが被らなくなるまで再発行する
        id = uuid.uuid4().hex
        while os.path.isdir('./movie/' + id):
            id = uuid.uuid4().hex

        # uuidと同名のディレクトリを作成する
        os.mkdir('./movie/' + id)

        # 非同期的に曲生成を開始する
        create_manager(id)

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

    return render_template(
        "preview.html",
        id=id
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

def create_manager(id):
    """
    「Twitter探し〜曲出力〜動画出力〜メール送信」までを管理する関数

    Parameter
    ---------
    id : str
        個人識別用uuid
    """
    try:
        mc.movie_create(id)
    except Exception as e:
        app.logger.error(str(e))
        app.logger.error(traceback.format_exc())

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if __name__=='__main__':
    port = 5000
    app.run(host="0.0.0.0", port=port, debug=True)
