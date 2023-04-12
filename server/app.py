from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db
from Apartment import Apartment
from Lease import Lease
from Tenant import Tenant

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False
app.json.compact = False


migrate = Migrate( app, db )
db.init_app( app )

api = Api(app)

class home(Resource):
    def get(self):
        return '<h1>Renter</h1>'
api.add_resource(home, "/")

class All_Apartments(Resource):
    def get(self):
        aps =[ap.to_dict() for ap in Apartment.query.all()]
        response = make_response(aps, 200)
        return response
    
    def post(self):
        new_apt = Apartment(number = request.form["number"])


        db.session.add(new_apt)
        db.session.commit()
        
        resp = new_apt.to_dict()
        response = make_response(resp, 201,)
        return response
api.add_resource(All_Apartments, "/apartments")

class one_apartment(Resource):
    def get(self, id):
        ap = Apartment.query.filter(Apartment.id== id).first()
        if ap != None:
            response = make_response(ap.first().to_dict(), 200)
        return response
    
    def patch(self, id):
        ap = Apartment.query.filter(Apartment.id== id).first()
        if ap != None:
            for attr in request.form:
                setattr(ap, attr, request.form[attr])
            db.session.add(ap)
            db.session.commit()
            
        response = make_response(ap.to_dict(), 200)

        return response
    
    def delete(self, id):
        ap = Apartment.query.filter(Apartment.id == id).first()
        resp = {}
        if ap != None:
            db.session.delete(ap)
            db.session.commit()
            resp = ap.to_dict()
            resp["deleted"] = "yes"
        else:
            resp = {}
            resp["deleted"] = "no"

        return make_response(resp, 200)
api.add_resource(one_apartment, "/apartment/<id>")

class All_Tenants(Resource):
    def get(self):
        aps =[ap.to_dict() for ap in Tenant.query.all()]
        response = make_response(aps, 200)
        return response
    
    def post(self):
        new_apt = Tenant(name = request.form["name"], age = request.form["age"])


        db.session.add(new_apt)
        db.session.commit()
        
        resp = new_apt.to_dict()
        response = make_response(resp, 201,)
        return response
api.add_resource(All_Tenants, "/tenants")

class one_tenant(Resource):
    def get(self, id):
        ap = Tenant.query.filter(Tenant.id== id).first()
        if ap != None:
            response = make_response(ap.first().to_dict(), 200)
        return response
    
    def patch(self, id):
        ap = Tenant.query.filter(Tenant.id== id).first()
        if ap != None:
            for attr in request.form:
                setattr(ap, attr, request.form[attr])
            db.session.add(ap)
            db.session.commit()
            
        response = make_response(ap.to_dict(), 200)

        return response
    
    def delete(self, id):
        ap = Tenant.query.filter(Tenant.id == id).first()
        resp = {}
        if ap != None:
            db.session.delete(ap)
            db.session.commit()
            resp = ap.to_dict()
            resp["deleted"] = "yes"
        else:
            resp = {}
            resp["deleted"] = "no"

        return make_response(resp, 200)
api.add_resource(one_tenant, "/tenant/<id>")


class All_Leases(Resource):
    def get(self):
        aps =[ap.to_dict() for ap in Lease.query.all()]
        response = make_response(aps, 200)
        return response
    
    def post(self):
        new_apt = Lease(rent = request.form["rent"])


        db.session.add(new_apt)
        db.session.commit()
        
        resp = new_apt.to_dict()
        response = make_response(resp, 201,)
        return response
api.add_resource(All_Leases, "/leases")

class one_lease(Resource):
    def get(self, id):
        ap = Lease.query.filter(Lease.id== id).first()
        if ap != None:
            response = make_response(ap.first().to_dict(), 200)
        return response
    
    def patch(self, id):
        ap = Lease.query.filter(Lease.id== id).first()
        if ap != None:
            for attr in request.form:
                setattr(ap, attr, request.form[attr])
            db.session.add(ap)
            db.session.commit()
            
        response = make_response(ap.to_dict(), 200)

        return response
    
    def delete(self, id):
        ap = Lease.query.filter(Lease.id == id).first()
        resp = {}
        if ap != None:
            db.session.delete(ap)
            db.session.commit()
            resp = ap.to_dict()
            resp["deleted"] = "yes"
        else:
            resp = {}
            resp["deleted"] = "no"

        return make_response(resp, 200)
api.add_resource(one_lease, "/lease/<id>")





if __name__ == '__main__':
    app.run( port = 5555, debug = True )