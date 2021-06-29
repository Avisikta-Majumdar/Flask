from flask import Flask


#Application Name :- app
app = Flask(__name__)

@app.route('/')
def Home(name):
    return "<h1>Welcome to This Tutorial</h1>"

@app.route('/info/<name>/')
def DynamicAllocation(name):
    return "<h1>Welcome {}, to This Tutorial</h1>".format(name)


if __name__ == '__main__':
    app.run()


