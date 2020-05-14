from .client import ClientsApi, ClientApi
from .worksheet import WorksheetsApi, WorksheetApi, WorksheetsCoApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/clients/<id>')
    api.add_resource(WorksheetsApi, '/api/worksheets')
    api.add_resource(WorksheetApi, '/api/worksheets/<id>')
    api.add_resource(WorksheetsCoApi, '/api/coworksheets/<co_id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')


