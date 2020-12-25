# -*- coding:utf-8 -*-

from flask import Flask，request, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/hello/<username>')
def hello_world(username):
    return 'Hello, %s!' % username

@app.route('/hello/<int:post_id>')
def hello_id(post_id):
    return 'Hello, you get a No.%d digree!' % post_id

@app.route('/main', methods=['GET', ' POST'])
def home():
    return '<h1>Home!</h1>'

@app.route('/signin', methods=['GET'])
def sighin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单：
    if request.form['username']=='admin' and request.form['password']=='password1':
         return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
# @app.route('/login')
# def login():
#     return 'Login'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login',next='/'))
#     print(url_for('hello_world', username='Mark Mo'))
#     print(url_for('hello_id', post_id=1))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)