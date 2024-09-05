from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except:
            return False


    def get_project_list(self):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            return client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])
        except WebFault as e:
            print(f"Soap error: {e}")
            return []