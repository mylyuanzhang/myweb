# -*- coding:utf-8 -*-

from flask import Flask, url_for
from flask import request
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<username>')
def hello_world(username):
    return 'Hello, %s!' % username

@app.route('/hello/<int:post_id>')
def hello_id(post_id):
    return 'Hello, you get a No.%d digree!' % post_id

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
1
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)