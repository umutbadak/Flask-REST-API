from models import db, ListingModel
from app import app

def populate_tables():
    print("Populating database...")
    with app.app_context():
        for i in range(10):
            address = "address_" + str(i)
            price = 400000 + i
            listing = ListingModel(address=address, price=price)
            db.session.add(listing)
        db.session.commit()

    print("Done!")

if __name__ == '__main__':
    populate_tables()
