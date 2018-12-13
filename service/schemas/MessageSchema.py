from marshmallow import Schema, fields

class MessageSchema(Schema):
    id = fields.String()
    event_id = fields.Integer()
    email_subject = fields.String()
    email_content = fields.String()
    timestamp = fields.DateTime()

message_schema = MessageSchema()
all_message_schema = MessageSchema(many=True)