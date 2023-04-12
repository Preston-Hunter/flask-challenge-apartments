from models import db
from sqlalchemy_serializer import SerializerMixin

class Apartment(db.Model, SerializerMixin):
    __tablename__ = "apartments"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    
    leases = db.relationship("Lease", backref="apartment")  
    serialize_rules = ("-leases.apartment")