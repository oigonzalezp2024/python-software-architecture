
from project.dependencies.delimitedData.delimitedData import DelimitedData

class DelimitedDataByTime(DelimitedData):

    def delimitedDataToOneMonth(self):
        self.getData("./project/data/json/promedioAbasSipsaMesMadr.json")
        self.oneMonth("fechaMesIni", pathEnd="./project/data/oneMonth/json/promedioAbasSipsaMesMadr.json")
        self.getData("./project/data/json/promediosSipsaCiudad.json")
        self.oneMonth("fechaCaptura", pathEnd="./project/data/oneMonth/json/promediosSipsaCiudad.json")
        self.getData("./project/data/json/promediosSipsaMesMadr.json")
        self.oneMonth("fechaMesIni", pathEnd="./project/data/oneMonth/json/promediosSipsaMesMadr.json")
        self.getData("./project/data/json/promediosSipsaParcial.json")
        self.oneMonth("enmaFecha", pathEnd="./project/data/oneMonth/json/promediosSipsaParcial.json")
        self.getData("./project/data/json/promediosSipsaSemanaMadr.json")
        self.oneMonth("fechaIni", pathEnd="./project/data/oneMonth/json/promediosSipsaSemanaMadr.json")
        return "ETL finalizada."

    def delimitedDataToQuarter(self):
        self.getData("./project/data/json/promedioAbasSipsaMesMadr.json")
        self.quarter("fechaMesIni", pathEnd="./project/data/quarter/json/promedioAbasSipsaMesMadr.json")
        self.getData("./project/data/json/promediosSipsaCiudad.json")
        self.quarter("fechaCaptura", pathEnd="./project/data/quarter/json/promediosSipsaCiudad.json")
        self.getData("./project/data/json/promediosSipsaMesMadr.json")
        self.quarter("fechaMesIni", pathEnd="./project/data/quarter/json/promediosSipsaMesMadr.json")
        self.getData("./project/data/json/promediosSipsaParcial.json")
        self.quarter("enmaFecha", pathEnd="./project/data/quarter/json/promediosSipsaParcial.json")
        self.getData("./project/data/json/promediosSipsaSemanaMadr.json")
        self.quarter("fechaIni", pathEnd="./project/data/quarter/json/promediosSipsaSemanaMadr.json")
        return "ETL finalizada."

    def delimitedDataToSemester(self):
        self.getData("./project/data/json/promedioAbasSipsaMesMadr.json")
        self.semester("fechaMesIni", pathEnd="./project/data/semester/json/promedioAbasSipsaMesMadr.json")
        self.getData("./project/data/json/promediosSipsaCiudad.json")
        self.semester("fechaCaptura", pathEnd="./project/data/semester/json/promediosSipsaCiudad.json")
        self.getData("./project/data/json/promediosSipsaMesMadr.json")
        self.semester("fechaMesIni", pathEnd="./project/data/semester/json/promediosSipsaMesMadr.json")
        self.getData("./project/data/json/promediosSipsaParcial.json")
        self.semester("enmaFecha", pathEnd="./project/data/semester/json/promediosSipsaParcial.json")
        self.getData("./project/data/json/promediosSipsaSemanaMadr.json")
        self.semester("fechaIni", pathEnd="./project/data/semester/json/promediosSipsaSemanaMadr.json")
        return "ETL finalizada."
