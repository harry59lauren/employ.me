from flask_restx import Namespace, Resource, fields
from app.models import db, Candidate as CandidateModel
from app.api.namespaces.candidates.schemas import CandidateSchema
from flask import request

CandidateApi = Namespace('candidates', description = 'inte')


candidate_schema = CandidateApi.model('Candidate', {
    'firstname' : fields.String(required=True, description=''),
    'middlename' : fields.String(required=True, description=''),
    'lastname' : fields.String( required=True, description=''),
    'city' : fields.String(required=True, description=''),
    'state' : fields.String(required=True, description='')
})

cs = CandidateSchema()

@CandidateApi.route('/')
class CandidateList(Resource):

    def get(self):
        candidates = CandidateModel.query.all()
        return cs.dump(candidates, many=True)
    
    def post(self):
        c = cs.load(request.json)
        db.session.add(c)
        db.session.commit()
        return cs.dump(c), 201


@CandidateApi.route('/<id>')
@CandidateApi.doc(params={'id': 'An ID'})
class Candidate(Resource):

    def get(self, id):
        c = CandidateModel.query.filter_by(id=id).first()
        return cs.dump(c)
