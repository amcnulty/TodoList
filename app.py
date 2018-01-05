from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
app.secret_key = 'wjur9HSn3iSlzg5qy0LpFbKGp7raRUH8Zfpv9UXR'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')