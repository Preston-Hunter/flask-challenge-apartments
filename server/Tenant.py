from models import db
from sqlalchemy_serializer import SerializerMixin

class Tenant(db.Model, SerializerMixin):
    __tablename__ = "tenants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer)
    
    leases = db.relationship("Lease", backref = "tenant")
    serialize_rules = ("-leases.tenant")

    @validates("age")
    def age_validate(self, key, age):
        if age >= 18:
            return age
        else:
            raise Exception("")