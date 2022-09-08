from flask import *
import random
import string
app = Flask(__name__)


@app.route("/")
def add():
    return render_template("addit.html")


@app.route("/product", methods=["POST"])
def product():
    if request.method == "POST":
        try:
            r = request.form["range"]
            result_str=' '.join(random.sample(string.ascii_lowercase, int(r)))
            return result_str
        except Exception as e:
            print(e)

if __name__== "__main__":
    app.run(debug=True)
