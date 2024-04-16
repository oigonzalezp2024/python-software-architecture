from project.dependencies.pythonFpdf2Table.pdfTable import PdfTable
from project.dependencies.pythonFpdf2PieChart.pieChart import PieChart
from project.data.data import data1, data2, data3, data4, data5
class EnterpriseCore(
    PdfTable, 
    PieChart
):
    def end(self):
        self.add_page()
        self.createTable(data1)
        self.multi_cell(w=5,h=15, text="")
        self.createTable(data2)
        self.multi_cell(w=5,h=15, text="")
        self.createTable(data3)
        self.multi_cell(w=5,h=15, text="")
        self.createTable(data4)

        self.add_page()
        self.dibujaGrafico(data5)

        self.output("./project/reports/enterpriseReport.pdf")
