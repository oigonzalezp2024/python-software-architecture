import enterprise.enterpriceDependecies.enterpriceDependecies
from enterprise.enterpriseCore.enterpriseCore import EnterpriseCore
from project.data.data import data1, data2, data3, data4, data5
from project.dependencies.clienteWebserviceSipsa.etl import etl
from project.extract.consultarInsumosSipsaMesMadr import pathFilea, wsdla, serviceMethoda, arg0a, fieldsa
from project.extract.promedioAbasSipsaMesMadr import pathFileb, wsdlb, serviceMethodb, arg0b, fieldsb
from project.extract.promediosSipsaCiudad import pathFilec, wsdlc, serviceMethodc, arg0c, fieldsc
from project.extract.promediosSipsaMesMadr import pathFiled, wsdld, serviceMethodd, arg0d, fieldsd
from project.extract.promediosSipsaParcial import pathFilee, wsdle, serviceMethode, arg0e, fieldse
from project.extract.promediosSipsaSemanaMadr import pathFilef, wsdlf, serviceMethodf, arg0f, fieldsf
from project.transformData.TransformData import TransformData

etl.controller(wsdla, serviceMethoda, arg0a, fieldsa, pathFilea)
etl.controller(wsdlb, serviceMethodb, arg0b, fieldsb, pathFileb)
etl.controller(wsdlc, serviceMethodc, arg0c, fieldsc, pathFilec)
etl.controller(wsdld, serviceMethodd, arg0d, fieldsd, pathFiled)
etl.controller(wsdle, serviceMethode, arg0e, fieldse, pathFilee)
etl.controller(wsdlf, serviceMethodf, arg0f, fieldsf, pathFilef)

delimitedDataFlow = TransformData()
delimitedDataFlow.delimitedDataToOneMonth()
delimitedDataFlow.delimitedDataToQuarter()
delimitedDataFlow.delimitedDataToSemester()

pdf = EnterpriseCore()
pdf.add_page()
pdf.createTable(data1)
pdf.multi_cell(w=5,h=15, text="")
pdf.createTable(data2)
pdf.multi_cell(w=5,h=15, text="")
pdf.createTable(data3)
pdf.multi_cell(w=5,h=15, text="")
pdf.createTable(data4)

pdf.add_page()
pdf.dibujaGrafico(data5)

pdf.output("./project/reports/enterpriseReport.pdf")
pdf.end()