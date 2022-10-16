from flask_restful import Api, Resource, reqparse, marshal_with, fields, abort
from models import ListingModel, db

api = Api()

# Parser for the requests
parser = reqparse.RequestParser()
parser.add_argument("address", type = str, required = True)
parser.add_argument("price", type = int, required = True)

# Schema for serializing responses
listing_fields = {
    'id' : fields.Integer,
    'address' : fields.String,
    'price' : fields.Integer
}

# Resource methods

class Listings(Resource):

    # List all items
    @marshal_with(listing_fields)
    def get(self):
        listings = ListingModel.query.all()
        return listings, 200

    # Create item
    @marshal_with(listing_fields)
    def post(self):
        args = parser.parse_args()
        listing = ListingModel(address=args['address'], price=args['price'])
        db.session.add(listing)
        db.session.commit()
        return listing, 201

class Listing(Resource):

    # Get single item
    @marshal_with(listing_fields)
    def get(self, id):
        listing = ListingModel.query.get(id)
        if listing is None:
            abort(404, message = "Resource is not found")
        return listing, 200

    # Update item
    @marshal_with(listing_fields)
    def put(self, id):
        args = parser.parse_args()
        listing = ListingModel.query.get(id)
        if listing is None:
            abort(404, message = "Resource is not found")
        listing.address = args['address']
        listing.price = args['price']
        db.session.commit()
        return listing, 200

    # Delete item
    @marshal_with(listing_fields)
    def delete(self, id):
        listing = ListingModel.query.get(id)
        if listing is None:
            abort(404, message = "Resource is not found")
        db.session.delete(listing)
        db.session.commit()
        return listing, 200

# Endpoints
BASE_URL = "/api/v1"

api.add_resource(Listings, BASE_URL + "/listings")
api.add_resource(Listing, BASE_URL + "/listings/<int:id>")