from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Company
from flask_restful import Resource

class ClientsApi(Resource):
    def get(self):
        companies = Company.objects().to_json()
        return Response(companies, mimetype="application/json", status=200)
    
    @jwt_required
    def post(self):
        body = request.get_json()
        company = Company(**body).save()
        id = company.id
        name = company.name_co
        return {'id': str(id), 'nama perusahaan': str(name)}, 200

class ClientApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Company.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        company = Company.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        company = Company.objects.get(id=id).to_json()
        return Response(company, mimetype="application/json", status=200)
        
        
