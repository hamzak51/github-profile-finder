from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def github_profile():
    if request.method == "POST":
        username = request.form.get("username")
        headers = {"Authorization": "token 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"}
        userdetails=requests.get(f"https://api.github.com/users/{username}", headers=headers).json()
        if "message" in userdetails and userdetails["message"] =="Not Found":
            return render_template('index.html', errorhtml="User not found!")

        return render_template('result.html', userdetails=userdetails)

    return render_template('index.html')
    


app.run(debug=True)
