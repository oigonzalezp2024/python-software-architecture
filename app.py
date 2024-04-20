import enterprise.enterpriceDependecies.enterpriceDependecies
from enterprise.enterpriseCore.enterpriseCore import EnterpriseCore
from enterprise.enterpriseFlaskFlow.EnterpriseFlaskFlow import EnterpriseFlaskFlow
from project.dependencies.clienteWebserviceSipsa.etl import etl
from project.dependencies.delimitedData.delimitedData import DelimitedData
from project.extract.consultarInsumosSipsaMesMadr import pathFilea, wsdla, serviceMethoda, arg0a, fieldsa
from project.extract.promedioAbasSipsaMesMadr import pathFileb, wsdlb, serviceMethodb, arg0b, fieldsb
from project.extract.promediosSipsaCiudad import pathFilec, wsdlc, serviceMethodc, arg0c, fieldsc
from project.extract.promediosSipsaMesMadr import pathFiled, wsdld, serviceMethodd, arg0d, fieldsd
from project.extract.promediosSipsaParcial import pathFilee, wsdle, serviceMethode, arg0e, fieldse
from project.extract.promediosSipsaSemanaMadr import pathFilef, wsdlf, serviceMethodf, arg0f, fieldsf

app = EnterpriseFlaskFlow(__name__)
delimitaConsulta = DelimitedData()

@app.route('/')
def helloW(name=None):
    return "bienvenido."

@app.route('/promedioAbasSipsaMesMadr')
def promedioAbasSipsaMesMadr(name=None):
    render = app.renderJson("promedioAbasSipsaMesMadr", "index.html", "./project/data/oneMonth/json/promedioAbasSipsaMesMadr.json")
    return render

@app.route('/promediosSipsaCiudad')
def promediosSipsaCiudad(name=None):
    render = app.renderJson("promediosSipsaCiudad", "index.html", "./project/data/oneMonth/json/promediosSipsaCiudad.json")
    return render

@app.route('/promediosSipsaMesMadr')
def promediosSipsaMesMadr(name=None):
    render = app.renderJson("promediosSipsaMesMadr", "index.html", "./project/data/oneMonth/json/promediosSipsaMesMadr.json")
    return render

@app.route('/promediosSipsaParcial')
def promediosSipsaParcial(name=None):
    render = app.renderJson("promediosSipsaParcial", "index.html", "./project/data/oneMonth/json/promediosSipsaParcial.json")
    return render

@app.route('/promediosSipsaSemanaMadr')
def promediosSipsaSemanaMadr(name=None):
    render = app.renderJson("promediosSipsaSemanaMadr", "index.html", "./project/data/oneMonth/json/promediosSipsaSemanaMadr.json")
    return render

@app.route('/generaEtl')
def generaEtl(name=None):
    etl.controller(wsdla, serviceMethoda, arg0a, fieldsa, pathFilea)
    etl.controller(wsdlb, serviceMethodb, arg0b, fieldsb, pathFileb)
    etl.controller(wsdlc, serviceMethodc, arg0c, fieldsc, pathFilec)
    etl.controller(wsdld, serviceMethodd, arg0d, fieldsd, pathFiled)
    etl.controller(wsdle, serviceMethode, arg0e, fieldse, pathFilee)
    etl.controller(wsdlf, serviceMethodf, arg0f, fieldsf, pathFilef)
    return "ETL finalizada."

@app.route('/oneMonth')
def oneMonth(name=None):
    delimitaConsulta.oneMonth("fechaMesIni", "./project/data/json/promedioAbasSipsaMesMadr.json", "./project/data/oneMonth/json/promedioAbasSipsaMesMadr.json")
    delimitaConsulta.oneMonth("fechaCaptura", "./project/data/json/promediosSipsaCiudad.json", "./project/data/oneMonth/json/promediosSipsaCiudad.json")
    delimitaConsulta.oneMonth("fechaMesIni", "./project/data/json/promediosSipsaMesMadr.json", "./project/data/oneMonth/json/promediosSipsaMesMadr.json")
    delimitaConsulta.oneMonth("enmaFecha", "./project/data/json/promediosSipsaParcial.json", "./project/data/oneMonth/json/promediosSipsaParcial.json")
    delimitaConsulta.oneMonth("fechaIni", "./project/data/json/promediosSipsaSemanaMadr.json", "./project/data/oneMonth/json/promediosSipsaSemanaMadr.json")
    return "ETL finalizada."

@app.route('/quarter')
def quarter(name=None):
    delimitaConsulta.quarter("fechaMesIni", "./project/data/json/promedioAbasSipsaMesMadr.json", "./project/data/quarter/json/promedioAbasSipsaMesMadr.json")
    delimitaConsulta.quarter("fechaCaptura", "./project/data/json/promediosSipsaCiudad.json", "./project/data/quarter/json/promediosSipsaCiudad.json")
    delimitaConsulta.quarter("fechaMesIni", "./project/data/json/promediosSipsaMesMadr.json", "./project/data/quarter/json/promediosSipsaMesMadr.json")
    delimitaConsulta.quarter("enmaFecha", "./project/data/json/promediosSipsaParcial.json", "./project/data/quarter/json/promediosSipsaParcial.json")
    delimitaConsulta.quarter("fechaIni", "./project/data/json/promediosSipsaSemanaMadr.json", "./project/data/quarter/json/promediosSipsaSemanaMadr.json")
    return "ETL finalizada."

@app.route('/semester')
def semester(name=None):
    delimitaConsulta.semester("fechaMesIni", "./project/data/json/promedioAbasSipsaMesMadr.json", "./project/data/semester/json/promedioAbasSipsaMesMadr.json")
    delimitaConsulta.semester("fechaCaptura", "./project/data/json/promediosSipsaCiudad.json", "./project/data/semester/json/promediosSipsaCiudad.json")
    delimitaConsulta.semester("fechaMesIni", "./project/data/json/promediosSipsaMesMadr.json", "./project/data/semester/json/promediosSipsaMesMadr.json")
    delimitaConsulta.semester("enmaFecha", "./project/data/json/promediosSipsaParcial.json", "./project/data/semester/json/promediosSipsaParcial.json")
    delimitaConsulta.semester("fechaIni", "./project/data/json/promediosSipsaSemanaMadr.json", "./project/data/semester/json/promediosSipsaSemanaMadr.json")
    return "ETL finalizada."

@app.route('/generaReporte')
def generaReporte(name=None):
    pdf = EnterpriseCore()
    pdf.end()
    return "Informes generados."
