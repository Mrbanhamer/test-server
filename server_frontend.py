from flask import Flask, redirect, url_for, request, render_template
from server_backend import add_new_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/info')
def info():
    return render_template('write_information.html')

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
    
@app.route('/write', methods=['POST', 'GET'])
def write_down():
    name = request.form['name']
    add_new_data(name)
    return redirect(url_for('/saved/<name>'))

@app.route('/saved/<name>')
def saved(name):
    return f"Name '{name}' saved succesfully!"

if __name__ == '__main__':
    app.run(debug=True)
