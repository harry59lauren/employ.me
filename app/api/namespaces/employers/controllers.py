from flask_restx import Namespace, Resource, fields
from app.models import db, Employer as EmployerModel
from app.api.namespaces.employers.schemas import EmployerSchema
from flask import request

EmployersAPI = Namespace('employers', description = 'interact with employers')

es = EmployerSchema()

@EmployersAPI.route('/')
class EmployerList(Resource):

    def get(self):
        employers = EmployerModel.query.all()
        return es.dump(employers, many=True)
    
    def post(self):
        e = es.load(request.json)
        db.session.add(e)
        db.session.commit()
        return es.dump(e), 201