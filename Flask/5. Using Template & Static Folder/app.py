from flask import Flask , render_template


App = Flask(__name__)

@App.route('/')
def Home():
    return render_template('base.html')

if __name__ == "__main__":
    App.run()

