from app import ma
from marshmallow import post_load
from app.models import Employer

class EmployerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employer
    
    id = ma.auto_field()
    name = ma.auto_field()

    @post_load
    def make_employer(self, data, **kwargs):
        return Employer(**data)