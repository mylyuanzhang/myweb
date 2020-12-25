# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

# @app.route('/hello/<username>')
# def hello_world(username):
#     return 'Hello, %s!' % username

# @app.route('/hello/<int:post_id>')
# def hello_id(post_id):
#     return 'Hello, you get a No.%d digree!' % post_id

# @app.route('/main', methods=['GET', ' POST'])
# def home():
#     return '<h1>Home!</h1>'
def login(username, password):
    if username=='admin' and password=='password1':
        return True
    return False

@app.route('/signin', methods=['GET'])
def sighin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # 需要从request对象读取表单：
    if login(username, password):
        return render_template('signin-passed.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

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