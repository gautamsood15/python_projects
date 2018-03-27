from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Method used : %s" % request.method


@app.route("/bacon", methods=['GET', 'POST'])
def baecon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "YOU are probably using GET"

if __name__ == "__main__":
    app.run()
