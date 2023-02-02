from flask import Flask, render_template

app = Flask(__name__)

@app.route("/datos")
def datos():
    nombre = "Roberto"
    lista1 = ["uno", "dos", "tres", "cuatro"]
    return render_template("datos.html", nombre=nombre, lista1=lista1)

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


if __name__ == '__main__':
    app.run(debug=True, port=3000)
