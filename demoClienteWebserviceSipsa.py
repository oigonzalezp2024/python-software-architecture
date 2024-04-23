import enterprise.enterpriceDependecies.enterpriceDependecies
from project.dependencies.clienteWebserviceSipsa.etl import etl
from project.extract.consultarInsumosSipsaMesMadr import pathFilea, wsdla, serviceMethoda, arg0a, fieldsa
from project.extract.promedioAbasSipsaMesMadr import pathFileb, wsdlb, serviceMethodb, arg0b, fieldsb
from project.extract.promediosSipsaCiudad import pathFilec, wsdlc, serviceMethodc, arg0c, fieldsc
from project.extract.promediosSipsaMesMadr import pathFiled, wsdld, serviceMethodd, arg0d, fieldsd
from project.extract.promediosSipsaParcial import pathFilee, wsdle, serviceMethode, arg0e, fieldse
from project.extract.promediosSipsaSemanaMadr import pathFilef, wsdlf, serviceMethodf, arg0f, fieldsf

etl.controller(wsdla, serviceMethoda, arg0a, fieldsa, pathFilea)
etl.controller(wsdlb, serviceMethodb, arg0b, fieldsb, pathFileb)
etl.controller(wsdlc, serviceMethodc, arg0c, fieldsc, pathFilec)
etl.controller(wsdld, serviceMethodd, arg0d, fieldsd, pathFiled)
etl.controller(wsdle, serviceMethode, arg0e, fieldse, pathFilee)
etl.controller(wsdlf, serviceMethodf, arg0f, fieldsf, pathFilef)
