from marshmallow import Schema, fields

class EmailSchema(Schema):
    id = fields.String()
    email = fields.String()
    first_name = fields.String()
    last_name = fields.String()

email_schema = EmailSchema()