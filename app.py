<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Goal - [Afrin Afsana]</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        /* CSS Styles */
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #e6f7ff; /* Light Blue Background */
            color: #1f3a68;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            text-align: center;
        }

        .container {
            background-color: #ffffff;
            padding: 50px 70px;
            border-radius: 15px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
            max-width: 650px;
            width: 90%;
            animation: slideIn 1s ease-out;
            border-top: 5px solid #007bff; /* Accent Border */
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            color: #007bff; /* Blue Title */
            font-size: 3em;
            margin-bottom: 5px;
            font-weight: 700;
        }

        h2 {
            color: #28a745; /* Green Subtitle */
            font-size: 1.6em;
            margin-top: 0;
            font-weight: 600;
        }

        p {
            font-size: 1.1em;
            line-height: 1.7;
            margin-bottom: 25px;
        }

        .goal-box {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
            border: 1px dashed #007bff;
        }

        .goal-box p {
            font-size: 1.2em;
            font-weight: 600;
            color: #dc3545; /* Red for emphasis */
            margin: 0;
        }

        .highlight {
            color: #ffc107; /* Yellow highlight */
            font-weight: 700;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }

        .tagline {
            margin-top: 40px;
            font-style: italic;
            color: #6c757d;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Hello! 👋</h1>
        
        <h2>My name is <span class="highlight">[Insert Your Name]</span></h2>
        
        <p>
            I am currently studying in <span class="highlight">Class XI (Eleven)</span> and I have chosen the <span class="highlight">Science</span> stream. I am dedicated and passionate about my education and career path.
        </p>

        <div class="goal-box">
            <p>
                My primary ambition is to become a <span style="color: #007bff;">**Respectable Officer**</span>,
                <br>and simultaneously score <span style="color: #28a745;">**Above 90% Marks**</span> in my academics.
            </p>
        </div>
        
        <p class="tagline">
            Committed to reaching my goals through hard work and determination.
        </p>
    </div>

</body>
</html>

