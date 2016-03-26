from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "word up, it's the code word"

if __name__ == "__main__":
    app.run()
