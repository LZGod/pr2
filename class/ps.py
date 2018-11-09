from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<html><body><p>It's friday, dudes!</p></body></html>"
if __name__ == '__main__':
    app.run(debug=False)

