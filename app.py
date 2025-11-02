            from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Afrin Afsana | Official Website</title>
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(to right, #fce4ec, #f8bbd0);
                color: #333;
                text-align: center;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #e91e63;
                margin-top: 50px;
                font-size: 40px;
            }
            p {
                font-size: 20px;
                margin: 10px auto;
                width: 80%;
                line-height: 1.6;
            }
            .card {
                background: white;
                width: 85%;
                max-width: 600px;
                margin: 20px auto;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .footer {
                margin-top: 30px;
                font-size: 14px;
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>✨ Afrin Afsana ✨</h1>
        <div class="card">
            <h2>🌸 About Me</h2>
            <p>Class 11 Science Student | Dreaming Big | Future Officer 👑</p>
        </div>

        <div class="card">
            <h2>🎯 My Goals</h2>
            <p>To study hard, score above 85%, and prepare for NDA & Paramedical exams with full dedication.</p>
        </div>

        <div class="card">
            <h2>🌼 My Hobbies</h2>
            <p>Studying, Writing, Designing, and Learning New Things 💻✨</p>
        </div>

        <div class="card">
            <h2>📩 Contact Me</h2>

        <div class="footer">
            <p>Made with ❤️ by Afrin Afsana</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()

