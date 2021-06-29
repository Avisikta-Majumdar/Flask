from flask import Flask , render_template

Story = Flask(__name__)

@Story.route('/The-Richest-Man-In-Babylon')
def TRMIB():
    return render_template('home.html')


@Story.route('/IKIGAI')
def IKIGAI():
    return render_template('Ikigai.html')

@Story.route("/")
def Home():
    return render_template("HomePage.html")

if __name__ == "__main__":
    Story.run(debug = True)
