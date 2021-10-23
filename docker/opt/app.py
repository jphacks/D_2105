from flask import Flask, render_template
app = Flask(__name__)

# ページ表示関係
@app.route('/')
def hello():
    return render_template(
        "index.html",
    )

@app.route('/<id>/accept')
def accept():
    return render_template(
        "accept.html",
    )

@app.route('/<id>/preview')
def preview():
    return render_template(
        "preview.html",
    )

@app.route('/error')
def error():
    return render_template(
        "error.html",
    )
# ページ表示関係 ここまで

if __name__=='__main__':
    port = 12345
    app.run(port=port, debug=True)