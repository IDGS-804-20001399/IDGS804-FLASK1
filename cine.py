from flask import Flask, render_template, request
import math

app = Flask(__name__)

class Calculos():
    nombre = ''
    compradores = 0
    boletos = 0
    tarjeta = 0
    subtotal = 0
    total = 0
    descuento = 0
    descuento_pesos = 0
    descuento_adicional = 0
    maximos_boletos = 0
    precio = 12

    def __init__(self, nombre, compradores, boletos, tarjeta):
        self.nombre = nombre
        self.compradores = compradores
        self.boletos = boletos
        self.tarjeta = tarjeta

    def procesar(self):
        self.subtotal = self.precio * self.boletos

        if (self.boletos > 5):
            self.descuento = 15
        elif (self.boletos >= 3):
            self.descuento = 10

        self.descuento_pesos = self.subtotal * self.descuento / 100
        self.total = self.subtotal - self.descuento_pesos

        if (self.tarjeta):
            self.descuento_adicional = self.total * 10 / 100
            self.total = self.total - self.descuento_adicional


    def validar_cantidad(self):
        self.maximos_boletos = self.compradores * 7
        return self.maximos_boletos >= self.boletos

@app.route("/cine")
def cine():
    return render_template("cine.html")

@app.route('/resultado', methods=["POST"])
def resultado():
    nombre = request.form.get("nombre")
    compradores = int(request.form.get("compradores"))
    boletos = int(request.form.get("boletos"))
    tarjeta = int(request.form.get("tarjeta"))
    calculos = Calculos(nombre, compradores, boletos, tarjeta)
    valido = calculos.validar_cantidad()
    calculos.procesar()
    # x1 = int(request.form.get("x1"))
    # y1 = int(request.form.get("y1"))
    # x2 = int(request.form.get("x2"))
    # y2 = int(request.form.get("y2"))
    # d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return render_template("resultado-cine.html", 
    nombre = calculos.nombre,
    compradores = calculos.compradores,
    maximos_boletos = calculos.maximos_boletos,
    boletos = calculos.boletos,
    precio = calculos.precio,
    subtotal = calculos.subtotal,
    descuento = calculos.descuento,
    descuento_pesos = calculos.descuento_pesos,
    descuento_adicional = calculos.descuento_adicional,
    total = calculos.total,
    valido = valido
    )
    pass

if __name__ == '__main__':
    app.run(debug=True, port=3000)
