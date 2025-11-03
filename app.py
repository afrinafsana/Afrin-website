from flask import Flask, render_template

# -------------------------------
# Create Flask app
# -------------------------------
app = Flask(__name__)

# -------------------------------
# Home Page Route
# -------------------------------
@app.route('/')
def home():
    return render_template('motivation.html')

# -------------------------------
# Game Page Route
# -------------------------------
@app.route('/game')
def game():
    return render_template('game.html')

# -------------------------------
# Run the app (for local testing)
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
