from models import db
from sqlalchemy_serializer import SerializerMixin

class Tenant(db.Model, SerializerMixin):
    __tablename__ = "tenants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer)
