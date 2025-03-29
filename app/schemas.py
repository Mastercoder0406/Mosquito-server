from marshmallow import Schema, fields, validate

class CrowdEventSchema(Schema):
    people_count = fields.Integer(required=True, validate=validate.Range(min=0))
    location = fields.String(required=True)
    density = fields.Float(required=True, validate=validate.Range(min=0, max=1))