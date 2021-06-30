from flask import *  
app = Flask(__name__)  
  
@app.route('/')  
def customer():  
   return render_template('customer.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      name = request.form['name']
      email = request.form['email']
      contact = request.form['contact']  
      pin = request.form['pin']
      
      return render_template("result_data.html",name = name , email = email , contact = contact , pin = pin)  
   
if __name__ == '__main__':  
   app.run(debug = True)  