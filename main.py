from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
df = pd.read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1/<word>")
def about(word):
    df = pd.read_csv("dictionary.csv")
    explanation = df.loc[df["word"] == word]["definition"].squeeze()
    dictionary = {"word": word,
                  "Definition": explanation}
    return dictionary


app.run()