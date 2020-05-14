from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Result
from flask_restful import Resource

class WorksheetsApi(Resource):
    def get(self):
        worksheets = Result.objects().to_json()
        return Response(worksheets, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        worksheet = Result(**body).save()
        id = worksheet.id
        return {'id': str(id)}, 200

class WorksheetApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Result.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        worksheet = Result.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        worksheet = Result.objects.get(id=id).to_json()
        return Response(worksheet, mimetype='application/json', status=200)

class WorksheetsCoApi(Resource):
    def get(self, co_id):
        worksheets = Result.objects(co_id=co_id).to_json()
        return Response(worksheets, mimetype="application/json", status=200)

        
 # f = request.files['file']
    # try:
    #     data_xls = pd.ExcelFile(f)
    #     list_sheet = data_xls.sheet_names

    #     response = json.dumps(list_sheet)
    #     print(response) 
    #     return {response} 
    # except:
    #     pass
    # return 'pass'

        
