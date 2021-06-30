from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home ():  
    return render_template("home.html")  
 
@app.route('/login')  
def login():  
    return render_template("login.html");

@app.route('/LoginAgain')  
def loginAgain():  
    return render_template("loginAgain.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'password':  
        return redirect(url_for("success"))  
    return redirect(url_for("loginAgain"))  
 
@app.route('/success')  
def success():  
    return "<center><br><br><h1>Logged in successfully</h1></center>body{background: #96ffb6;}"  
  
if __name__ == '__main__':  
    app.run(debug = True)