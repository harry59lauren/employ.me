from app import ma
from marshmallow import post_load, fields
from marshmallow.validate import OneOf
from app.models import Candidate, CandidateEmploymentHistory
from app.api.namespaces.employers.schemas import EmployerSchema


class CandidateEmploymentHistorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = CandidateEmploymentHistory
    
    id = ma.auto_field()
    employment_type = fields.Str(validate=OneOf(["FULLTIME","PARTTIME","SELF-EMPLOYED","CONTRACT","INTERNSHIP","APPRENCTICESHIP","FREELANCE"]))
    city = ma.auto_field()
    state = ma.auto_field()
    startdate = fields.Date(format='%d-%m-%Y')
    enddate = fields.Date(format='%d-%m-%Y')
    description = ma.auto_field()
    employer_id = ma.auto_field(required=False)
    employer = fields.Nested(EmployerSchema)

    @post_load
    def make_employment_history_entry(self, data, **kwargs):
        return CandidateEmploymentHistory(**data)


class CandidateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Candidate
    
    id = ma.auto_field()
    firstname = ma.auto_field()
    middlename = ma.auto_field()
    lastname = ma.auto_field()
    city = ma.auto_field()
    state = ma.auto_field()
    employment_history = fields.List(fields.Nested(CandidateEmploymentHistorySchema))
    link = fields.Function(lambda obj :  '/candidates/{}'.format(obj.id))

    @post_load
    def make_candidate(self, data, **kwargs):
        return Candidate(**data)