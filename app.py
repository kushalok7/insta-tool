from flask import Flask
import random

app = Flask("KUSH")

captions = [
    "Stay focused 🔥",
    "Hustle hard 💯",
    "No excuses 🚀",
    "Keep growing 💪"
]

hashtags = [
    "#viral", "#reels", "#explore", "#trending",
    "#instagood", "#motivation", "#success"
]

@app.route('/')
def home():
    return """
    <h1>Insta Tool 🚀</h1>
    <button onclick="getData()">Generate</button>
    <p id="result"></p>

    <script>
    function getData(){
        fetch('/all')
        .then(res => res.text())
        .then(data => {
            document.getElementById('result').innerText = data;
        });
    }
    </script>
    """

@app.route('/all')
def all_data():
    cap = random.choice(captions)
    tags = " ".join(random.sample(hashtags, 4))
    return f"{cap}\\n\\n{tags}"

import os

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
