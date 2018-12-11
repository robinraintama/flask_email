from service import db

class Messages(db.Model):
    __tablename__           = 'tr_messages'
    id                      = db.Column(db.Integer, primary_key = True, auto_increament = True)
    event_id                = db.Column(db.Integer)
    email_subject           = db.Column(db.String(200))
    email_content           = db.Column(db.String(500))