from flask import Flask

Application = Flask(__name__)

@Application.route("/")
def Home():
    return "Hello , World!!"


@Application.route("/info/<name>")
def Dynamic(name):
    return "Name :- {}".format(name)


if __name__ == "__main__":
    Application.run()
