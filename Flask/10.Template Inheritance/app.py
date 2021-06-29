from flask import Flask , render_template

app = Flask(__name__)

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/basic2')
def basic2():
    return render_template('basic2.html')

@app.route('/')
def home():
    return "Got to /basic or /basic2"

if __name__=="__main__":
    app.run()