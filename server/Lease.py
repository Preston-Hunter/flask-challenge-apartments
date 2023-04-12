from models import db
from sqlalchemy_serializer import SerializerMixin

class Lease(db.Model, SerializerMixin):
    __tablename__ = "leases"
    id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)