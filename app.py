from flask import Flask, redirect, url_for, request, render_template_string
import requests

app = Flask(__name__)

url = "https://zenquotes.io/api/random"

template = """
<!DOCTYPE html>
<html>
   <body>
      <h1>Quote Generator</h1>
      <form method = "POST" action = "/">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nm" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
"""


@app.route("/success/<name>")
def success(name):
    response = requests.get(url)
    print(response.text)
    return f'Hi {name}, your quote is "{response.json()[0]["q"]}" - {response.json()[0]["a"]}'


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name=user))
    return render_template_string(template)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
