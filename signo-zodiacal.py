from flask import Flask, render_template, request
from datetime import date
import math

app = Flask(__name__)

año = 0
mes = 0
dia = 0
nombre = ""
apaterno = ""
amaterno = ""
sexo = 0

@app.route("/")
def puntos():
    return render_template("zodiaco-index.html")

@app.route('/quiz', methods=["POST"])
def quiz():
    global año 
    global mes 
    global dia
    global nombre 
    global apaterno 
    global amaterno
    global sexo
    año = int(request.form.get("year"))
    mes = int(request.form.get("mes"))
    dia = int(request.form.get("dia"))
    nombre = request.form.get("nombre")
    apaterno = request.form.get("apaterno")
    amaterno = request.form.get("amaterno")
    sexo = int(request.form.get("sexo"))
    return render_template("zodiaco-quiz.html")

@app.route('/resultado', methods=["POST"])
def resultado():
    global año 
    global mes 
    global dia
    global nombre 
    global apaterno 
    global amaterno
    global sexo
    rata = [1936, 1948, 1960, 1972, 1984, 1996, 2008]
    buey = [1937, 1949, 1961, 1973, 1985, 1997, 2009]
    tigre = [1938, 1950, 1962, 1974, 1986, 1998, 2010]
    conejo = [1939, 1951, 1963, 1975, 1987, 1999, 2011]
    dragon = [1940, 1952, 1964, 1976, 1988, 2000, 2012]
    serpiente = [1941, 1953, 1965, 1977, 1989, 2001, 2013]
    caballo = [1942, 1954, 1966, 1978, 1990, 2002, 2014]
    cabra = [1943, 1955, 1967, 1979, 1991, 2003, 2015]
    mono = [1944, 1956, 1968, 1980, 1992, 2004, 2016]
    gallo = [1945, 1957, 1969, 1981, 1993, 2005, 2017]
    perro = [1946, 1958, 1970, 1982, 1994, 2006, 2018]
    cerdo = [1947, 1959, 1971, 1983, 1995, 2007, 2019]
    img = ''
    signo = ''
    p1 = int(request.form.get("p1"))
    p2 = int(request.form.get("p2"))
    p3 = int(request.form.get("p3"))
    p4 = int(request.form.get("p4"))
    p5 = int(request.form.get("p5"))
    res = p1 + p2 + p3 + p4 + p5
    today = date.today()
    if (año in rata):
        signo = 'rata'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Rata-300x257.jpg'
    elif (año in buey):
        signo = 'buey'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Buey-300x257.jpg'
    elif (año in tigre):
        signo = 'tigre'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Tigre-300x257.jpg'
    elif (año in conejo):
        signo = 'conejo'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Conejo-300x257.jpg'
    elif (año in dragon):
        signo = 'dragon'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Dragon-300x257.jpg'
    elif (año in serpiente):
        signo = 'serpiente'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Serpiente-300x257.jpg'
    elif (año in caballo):
        signo = 'caballo'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Caballo-300x257.jpg'
    elif (año in cabra):
        signo = 'cabra'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cabra-300x257.jpg'
    elif (año in mono):
        signo = 'mono'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Mono-300x257.jpg'
    elif (año in gallo):
        signo = 'gallo'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Gallo-300x257.jpg'
    elif (año in perro):
        signo = 'perro'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Perro-300x257.jpg'
    elif (año in cerdo):
        signo = 'cerdo'
        img = 'http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cerdo-300x257.jpg'

    edad = today.year - año - ((today.month, today.day) < (mes, dia))

    return render_template("zodiaco-res.html", nombre = nombre, apaterno = apaterno, amaterno = amaterno, edad = edad, res = res, img = img, signo = signo)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
