from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/punto")
def puntos():
    return render_template("puntos.html")

@app.route('/resultado', methods=["POST"])
def resultado():
    x1 = int(request.form.get("x1"))
    y1 = int(request.form.get("y1"))
    x2 = int(request.form.get("x2"))
    y2 = int(request.form.get("y2"))
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return render_template("resultado-puntos.html", x1=x1, y1=y1, x2=x2, y2=y2, d=d)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
