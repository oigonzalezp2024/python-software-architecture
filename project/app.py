from dependencies.flaskFlow.flaskFlow import FlaskFlow

app = FlaskFlow(__name__)

@app.route('/')
def helloW(name=None):
    render = app.renderJson("promedioAbasSipsaMesMadr", "index.html", "./data/json/promedioAbasSipsaMesMadr.json")
    return render

@app.route('/promedioAbasSipsaMesMadr')
def promedioAbasSipsaMesMadr(name=None):
    render = app.renderJson("promedioAbasSipsaMesMadr", "index.html", "./data/json/promedioAbasSipsaMesMadr.json")
    return render

@app.route('/promediosSipsaCiudad')
def promediosSipsaCiudad(name=None):
    render = app.renderJson("promediosSipsaCiudad", "index.html", "./data/json/promediosSipsaCiudad.json")
    return render

@app.route('/promediosSipsaMesMadr')
def promediosSipsaMesMadr(name=None):
    render = app.renderJson("promediosSipsaMesMadr", "index.html", "./data/json/promediosSipsaMesMadr.json")
    return render

@app.route('/promediosSipsaParcial')
def promediosSipsaParcial(name=None):
    render = app.renderJson("promediosSipsaParcial", "index.html", "./data/json/promediosSipsaParcial.json")
    return render

@app.route('/promediosSipsaSemanaMadr')
def promediosSipsaSemanaMadr(name=None):
    render = app.renderJson("promediosSipsaSemanaMadr", "index.html", "./data/json/promediosSipsaSemanaMadr.json")
    return render