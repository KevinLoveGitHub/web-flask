from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/login')
def hello():
    return 'please login'


@app.route('/username/<username>')
def show_username(username):
    return 'Your username %s' % username


@app.route('/id/<int:user_id>')
def show_userid(user_id):
    return 'Your userid %d' % user_id


@app.route('/url')
def show_url():
    return '不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去'


@app.route('/url2/')
def show_url2():
    return '访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误'


@app.route('/test')
def test(): pass


with app.test_request_context():
    print(url_for('test', next='/'))
    print(url_for('static', filename='test.html'))


@app.route('/methods', methods=['GET', 'POST'])
def methods():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'


@app.route('/template/')
@app.route('/template/<userid>')
def template(userid=None):
    return render_template('test.html', userid=userid)


if __name__ == '__main__':
    # 开启调试模式
    app.run(debug=True)
