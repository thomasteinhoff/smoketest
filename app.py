from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Smoke Test!"

@app.route("/status")
def status():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
