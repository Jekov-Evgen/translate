from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.route("/answer", methods=["POST"])
def answer_page():
    data = request.form.get("enter_text")
    traslator = Translator(from_lang="russian", to_lang="english")
    translation = traslator.translate(data)
    return render_template("answer_page.html", translation=translation, data=data)

if __name__ == "__main__":
    app.run(debug=True)