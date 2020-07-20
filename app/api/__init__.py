from flask_restx import Api
from app.api.namespaces.candidates.controllers import CandidateApi
from app.api.namespaces.employers.controllers import EmployersAPI

api = Api(
    title='Hire.me REST API',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(CandidateApi)
api.add_namespace(EmployersAPI)