from flask import Flask


#Application Name :- BasicApplication
BasicApplication = Flask(__name__)

@BasicApplication.route('/')#This is a decorator
#in .route we are passing link address
def Home(name="Avisikta Majumdar"):
    return "<h1>Welcome {} to This Tutorial</h1>".format(name)

if __name__ == '__main__':
    BasicApplication.run()


