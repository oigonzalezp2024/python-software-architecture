import enterprise.enterpriceDependecies.enterpriceDependecies
from enterprise.enterpriseCore.enterpriseCore import EnterpriseCore
from project.data.data import data1, data2, data3, data4, data5

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