from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "!Hola Mundo!"

# Pasamos un string
@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}"

# Pasamos parametros int
@app.route("/numero/<int:n>")
def numero(n):
    return f"Numero: {n}"

# Pasamos mas de un parametro
@app.route("/user/<int:id>/<string:username>")
def usern(id, username):
    return f"ID: {id} nombre: {username}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es : {n1 + n2}"



if __name__ == '__main__':
    app.run(debug=True, port=3000)
