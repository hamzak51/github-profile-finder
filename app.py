from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

@app.route("/", methods=['GET', 'POST'])
def github_profile():
    if request.method == "POST":
        username = request.form.get("username")

        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        userdetails=requests.get(f"https://api.github.com/users/{username}", headers=headers).json()
        
        if "message" in userdetails and userdetails["message"] =="Not Found":
            return render_template('index.html', errorhtml="User not found!")

        return render_template('result.html', userdetails=userdetails)

    return render_template('index.html')
    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
