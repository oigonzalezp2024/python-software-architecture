from project.dependencies.pythonFpdf2Table.pdfTable import PdfTable
from project.dependencies.pythonFpdf2PieChart.pieChart import PieChart

class EnterpriseCore(
    PdfTable, 
    PieChart
):
    def end(self):
        print("Ejecución exitosa. Revice el directorio de reportes.")
        print(">>> ./reports\n")
