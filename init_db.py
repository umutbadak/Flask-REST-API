from models import db
from app import app
def create_tables():
    print("Creating database tables...")
    with app.app_context():
        db.create_all()
    print("Done!")

if __name__ == '__main__':
    create_tables()