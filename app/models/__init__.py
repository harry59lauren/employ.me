from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80) , nullable=False)
    lastname = db.Column(db.String(80) , nullable=False)
    middlename = db.Column(db.String(80) , nullable=True)
    city = db.Column(db.String(80) , nullable=True)
    state = db.Column(db.String(80) , nullable=True)

    employment_history = db.relationship('CandidateEmploymentHistory', backref='candidate', lazy=True)


class CandidateEmploymentHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employment_type = db.Column(db.Enum("FULLTIME","PARTTIME","SELF-EMPLOYED","CONTRACT","INTERNSHIP","APPRENCTICESHIP","FREELANCE"))
    city = db.Column(db.String())
    state = db.Column(db.String())
    startdate = db.Column(db.Date())
    enddate = db.Column(db.Date())
    description = db.Column(db.String())
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'),
        nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'),
        nullable=False)
    employer = db.relationship('Employer', backref=db.backref('CandidateEmploymentHistory', lazy=True), uselist=False)
    
    
    
    
    
    
    
    '''
CandidateEmplomentHisotry
    - id
    - cid (references candidate id)
    - employer_id
    - employement_type : [FULLTIME, PARTTIME, SELF-EMPLOYED, CONTRACT, INTERNSHIP, APPRENCTICESHIP, FREELANCE]
    - city
    - state
    - country
    - start : MM / YYYY
    - enddate : MM / YYYY
    - description (responsibilities)
'''