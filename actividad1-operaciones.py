
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/operaciones", methods=["GET", "POST"])
def operaciones():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        operacion = int(request.form.get("operacion"))
        if operacion == 1:
            return f"<h1>La suma es: {num1 + num2}</h1>"
        elif operacion == 2:
            return f"<h1>La resta es: {num1 - num2}</h1>"
        elif operacion == 3:
            return f"<h1>La multiplicacion es: {num1 * num2}</h1>"
        elif operacion == 4:
            return f"<h1>La division es: {num1 / num2}</h1>"
    else:
        return '''
            <form action="/operaciones" method="POST">
                <label>N1: </label>
                <input type="text" name="num1"/><br><br>
                <label>N2: </label>
                <input type="text" name="num2"/><br><br>
                <p>Selecciona la operacion:</p
                <div>
                    <input type="radio" id="suma" name="operacion" value="1">
                    <label for="suma">Suma</label>
                </div>
                <div>
                    <input type="radio" id="resta" name="operacion" value="2">
                    <label for="resta">Resta</label>
                </div>
                <div>
                    <input type="radio" id="multi" name="operacion" value="3">
                    <label for="multi">Multiplicacion</label>
                </div>
                <div>
                    <input type="radio" id="divi" name="operacion" value="4">
                    <label for="divi">Division</label>
                </div>
                <input type="submit" value="Calcular"/>
            </from>
        '''


if __name__ == '__main__':
    app.run(debug=True, port=3000)
