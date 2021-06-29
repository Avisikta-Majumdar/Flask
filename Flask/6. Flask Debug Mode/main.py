from flask import Flask


#Application Name :- app
app = Flask(__name__)

@app.route('/')
def Home():
    return "<h1>Welcome to This Tutorial</h1>"

@app.route('/info/<name>/')
def DynamicAllocation(name):
    return "the 10th element of this name {}".format(name[9])


if __name__ == '__main__':
    app.run(debug = True)


    '''
    Put debug = True at the time of development ,
    not at deployment
    
    If debug is True this means it will show / trace the error 
    '''