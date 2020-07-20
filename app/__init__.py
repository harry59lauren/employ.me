from flask import Flask, request
from datetime import datetime, date
from app.models import db, Candidate
from flask_marshmallow import Marshmallow

ma = Marshmallow()

from app.api import api
from app.api.namespaces.candidates.schemas import CandidateEmploymentHistorySchema



def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hire.db'

    api.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        cand = Candidate(firstname='Harry', middlename='Ian', lastname='Laurenceau',
        city='Chicago', state='MD')
        db.session.add(cand)
        db.session.commit()
    
    ma.init_app(app)

    @app.route('/health')
    def healthcheck():
        return {'status' : 'UP'}

    @app.route('/history/<int:id>', methods=['POST'])
    def add_history(id):
        ceh = CandidateEmploymentHistorySchema()
        employment_history = request.json
        #employment_history['startdate'] = datetime.strptime(employment_history['startdate'], '%d-%m-%Y')
        #employment_history['enddate'] = datetime.strptime(employment_history['enddate'], '%d-%m-%Y')
        c = ceh.load(employment_history)
        print(c, type(c.startdate))
        return 'success'

    return app