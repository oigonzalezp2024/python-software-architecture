from project.dependencies.flaskFlow.flaskFlow import FlaskFlow

class EnterpriseFlaskFlow(
    FlaskFlow
):
    def end(self):
        print("Ejecución exitosa. Revice el directorio de reportes.")
        print(">>> ./reports\n")
