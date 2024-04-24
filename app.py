import json
import enterprise.enterpriceDependecies.enterpriceDependecies
from enterprise.enterpriseCore.enterpriseCore import EnterpriseCore
from enterprise.enterpriseFlaskFlow.EnterpriseFlaskFlow import EnterpriseFlaskFlow
from project.dependencies.clienteWebserviceSipsa.etl import etl
from project.dependencies.delimitedData.delimitedData import DelimitedData
from project.dependencies.transformData.transformData import TransformData
from project.extract.consultarInsumosSipsaMesMadr import pathFilea, wsdla, serviceMethoda, arg0a, fieldsa
from project.extract.promedioAbasSipsaMesMadr import pathFileb, wsdlb, serviceMethodb, arg0b, fieldsb
from project.extract.promediosSipsaCiudad import pathFilec, wsdlc, serviceMethodc, arg0c, fieldsc
from project.extract.promediosSipsaMesMadr import pathFiled, wsdld, serviceMethodd, arg0d, fieldsd
from project.extract.promediosSipsaParcial import pathFilee, wsdle, serviceMethode, arg0e, fieldse
from project.extract.promediosSipsaSemanaMadr import pathFilef, wsdlf, serviceMethodf, arg0f, fieldsf

app = EnterpriseFlaskFlow(__name__)
delimitaConsulta = DelimitedData()

class TransformDataPath(TransformData):

    def businessLogic(self, data:object)->list:
        casos = []
        ciudades = []
        for i in data:
            ciudad = self.transMunicipio(str(i['ciudad']))
            producto = self.transProducto(str(i['producto']))
            caso = str("./static/images/")+str(ciudad+producto.capitalize())+str(".png")
            if(ciudad not in ciudades):
                rr = 2
                for i in ciudades:
                    if(i in ciudad):
                        rr = 1
                        break
                    if(ciudad in i):
                        rr = 1
                        ciudad = i
                        caso = str(ciudad+producto.capitalize())
                        break
                if(rr==2):
                    ciudades.append(ciudad)
            if(caso not in casos):
                casos.append(caso)
        return [{"image":casos}]
    
@app.route('/')
def helloW(name=None):
    render = app.renderJson("promedioAbasSipsaMesMadr", "index.html", "./project/data/oneMonth/json/promedioAbasSipsaMesMadr.json")
    return render

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

@app.route('/ciudad')
def ciudades(name=None):
    ttt = TransformDataPath()
    ttt.controller(
        "./project/data/oneMonth/json/promediosSipsaCiudad.json",
        "./project/data/transformedData/adminPath/pathsEnd.json",
        )
    render = app.renderJson("promediosSipsaSemanaMadr", "graficosLineas.html", "./project/data/transformedData/adminPath/pathsEnd.json")
    return render