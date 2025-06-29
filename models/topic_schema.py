from marshmallow import Schema, fields, validate


class MCQSchema(Schema):
    question = fields.String(required=True, validate=validate.Length(min=1))
    options = fields.List(
        fields.String(validate=validate.Length(min=1)),
        required=True,
        validate=validate.Length(equal=4),  # at least two options
    )


class TopicSchema(Schema):
    topic = fields.String(required=True, validate=validate.Length(min=1))
    mcq = fields.List(
        fields.Nested(MCQSchema), required=True, validate=validate.Length(min=1)
    )
