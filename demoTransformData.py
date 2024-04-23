import enterprise.enterpriceDependecies.enterpriceDependecies
from project.dependencies.transformData.transformData import TransformData

pathJson = "./project/data/oneMonth/json/promediosSipsaCiudad.json"
pathEnd = "./project/data/transformedData/json/transformedData.json"
TransformData().controller(pathJson, pathEnd)
