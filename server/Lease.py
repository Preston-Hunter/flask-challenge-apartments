from models import db
from sqlalchemy_serializer import SerializerMixin

class Lease(db.Model, SerializerMixin):
    __tablename__ = "leases"
    id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)

    apartment_id = db.Column(db.Integer, db.ForeignKey("apartments.id"))
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.id"))
    serialize_rules = ("-tenant.leases", "-apartment.leases")