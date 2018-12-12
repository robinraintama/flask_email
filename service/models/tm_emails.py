from service import db

class Emails(db.Model):
    __tablename__           = 'tm_emails'
    id                      = db.Column(db.String(30), primary_key=True)
    email                = db.Column(db.String(190))
    first_name           = db.Column(db.String(100))
    last_name           = db.Column(db.String(100))