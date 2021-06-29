'''
Jinja2 is a modern day templating language for Python developers. It was made after Django's template.
It is used to create HTML, XML or other markup formats that are returned to the user via an HTTP request.
'''
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def Home():
    name="Avisikta Majumdar"
    dept="C.S.E."
    Passing_year = 2022
    return render_template("base.html",my_name = name , dept = dept , Passing_year = Passing_year)

if __name__=="__main__":
    app.run(debug=True)