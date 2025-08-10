from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def github_profile():
    if request.method == "POST":
        username = request.form.get("username")
        userdetails=requests.get(f"https://api.github.com/users/{username}").json()
        if "message" in userdetails and userdetails["message"] =="Not Found":
            return render_template('index.html', errorhtml="User not found!")

        return render_template('result.html', userdetails=userdetails)

    return render_template('index.html')
    


app.run(debug=True)
