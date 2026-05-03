from flask import Flask, request
from helper import form, hello_world, get_help

app = Flask(__name__)
@app.route('/')
def home():
    return hello_world()

@app.route('/help.html')
def help():
    return get_help()

@app.route('/form', methods=['GET', 'POST'])
def login():
    return form()

@app.route('/user/<string:username>')     #by default, string is used, but you can specify other types like int, float, path, etc.  
def user(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True)



