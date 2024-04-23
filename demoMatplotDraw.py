import enterprise.enterpriceDependecies.enterpriceDependecies
from project.dependencies.matplotDraw.matplotDraw import MatplotDraw

matplotDraw1 = MatplotDraw()
data = matplotDraw1.readFileJson("./project/data/transformedData/json/transformedData.json")
matplotDraw1.pathEnd("./project/data/transformedData/images/")
matplotDraw1.getLineCharts(data)
