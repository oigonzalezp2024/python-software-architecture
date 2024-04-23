
from project.dependencies.delimitedData.delimitedData import DelimitedData

class DelimitedDataByTime(DelimitedData):

    def delimitedDataToOneMonth(self):
        self.oneMonth("fechaMesIni", "./project/data/json/promedioAbasSipsaMesMadr.json", "./project/data/oneMonth/json/promedioAbasSipsaMesMadr.json")
        self.oneMonth("fechaCaptura", "./project/data/json/promediosSipsaCiudad.json", "./project/data/oneMonth/json/promediosSipsaCiudad.json")
        self.oneMonth("fechaMesIni", "./project/data/json/promediosSipsaMesMadr.json", "./project/data/oneMonth/json/promediosSipsaMesMadr.json")
        self.oneMonth("enmaFecha", "./project/data/json/promediosSipsaParcial.json", "./project/data/oneMonth/json/promediosSipsaParcial.json")
        self.oneMonth("fechaIni", "./project/data/json/promediosSipsaSemanaMadr.json", "./project/data/oneMonth/json/promediosSipsaSemanaMadr.json")
        return "ETL finalizada."

    def delimitedDataToQuarter(self):
        self.quarter("fechaMesIni", "./project/data/json/promedioAbasSipsaMesMadr.json", "./project/data/quarter/json/promedioAbasSipsaMesMadr.json")
        self.quarter("fechaCaptura", "./project/data/json/promediosSipsaCiudad.json", "./project/data/quarter/json/promediosSipsaCiudad.json")
        self.quarter("fechaMesIni", "./project/data/json/promediosSipsaMesMadr.json", "./project/data/quarter/json/promediosSipsaMesMadr.json")
        self.quarter("enmaFecha", "./project/data/json/promediosSipsaParcial.json", "./project/data/quarter/json/promediosSipsaParcial.json")
        self.quarter("fechaIni", "./project/data/json/promediosSipsaSemanaMadr.json", "./project/data/quarter/json/promediosSipsaSemanaMadr.json")
        return "ETL finalizada."

    def delimitedDataToSemester(self):
        self.semester("fechaMesIni", "./project/data/json/promedioAbasSipsaMesMadr.json", "./project/data/semester/json/promedioAbasSipsaMesMadr.json")
        self.semester("fechaCaptura", "./project/data/json/promediosSipsaCiudad.json", "./project/data/semester/json/promediosSipsaCiudad.json")
        self.semester("fechaMesIni", "./project/data/json/promediosSipsaMesMadr.json", "./project/data/semester/json/promediosSipsaMesMadr.json")
        self.semester("enmaFecha", "./project/data/json/promediosSipsaParcial.json", "./project/data/semester/json/promediosSipsaParcial.json")
        self.semester("fechaIni", "./project/data/json/promediosSipsaSemanaMadr.json", "./project/data/semester/json/promediosSipsaSemanaMadr.json")
        return "ETL finalizada."
