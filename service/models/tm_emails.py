from service import db

class Emails(db.Model):
    __tablename__           = 'tm_emails'
    id                      = db.Column(db.String(30))
    event_id                = db.Column(db.String(190))
    email_subject           = db.Column(db.String(100))
    email_content           = db.Column(db.String(100))