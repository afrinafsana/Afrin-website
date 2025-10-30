from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Afrin 💖</h1><p>Your website is live now!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
