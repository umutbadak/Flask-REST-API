import requests
import unittest
from app import app
from models import db

# End points configuration
API_URL = "http://127.0.0.1:5000/api/v1"
RESOURCE = "/listings"


class TestApiMethods(unittest.TestCase):
    # Creates empty db tables before each test case
    def setUp(self):
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drops db tables after each test case
        with app.app_context():
            db.drop_all()

    def test_post(self):
        # POST a new item
        # Check status code
        # Check if newly created item has correct values
        # Check if 'Content-Type' header is correct
        new_listing = {'address' : 'address1', 'price' : 450001}
        response = requests.post(API_URL + RESOURCE, json = new_listing)
        self.assertEqual(response.status_code, 201)
        res_obj = response.json()
        self.assertEqual(res_obj['address'], new_listing['address'])
        self.assertEqual(res_obj['price'], new_listing['price'])
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_get_all(self):
        # GET all items
        # Check status code
        # Check if empty list is returned
        # Check if 'Content-Type' header is correct
        response = requests.get(API_URL + RESOURCE)
        self.assertEqual(response.status_code, 200)
        res_obj = response.json()
        self.assertEqual(res_obj, [])
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_get(self):
        # POST a new item
        # Check status code
        # GET newly created item
        # Check status code
        # Check if get returns item with correct values
        # Check if 'Content-Type' header is correct
        new_listing = {'address': 'address2', 'price': 450002}
        response = requests.post(API_URL + RESOURCE, json=new_listing)
        res_obj = response.json()
        self.assertEqual(response.status_code, 201)
        listing_id = res_obj['id']
        response = requests.get(API_URL + RESOURCE + f"/{listing_id}")
        self.assertEqual(response.status_code, 200)
        res_obj = response.json()
        self.assertEqual(res_obj['address'], new_listing['address'])
        self.assertEqual(res_obj['price'], new_listing['price'])
        self.assertEqual (response.headers['Content-Type'], 'application/json')

    def test_put(self):
        # POST a new item
        # Check status code
        # Get newly created item
        # PUT item with new values
        # Check if PUT updates item with correct values
        # Check if 'Content-Type' header is correct
        new_listing = {'address': 'address3', 'price': 450003}
        response = requests.post(API_URL + RESOURCE, json=new_listing)
        res_obj = response.json()
        self.assertEqual(response.status_code, 201)
        listing_id = res_obj['id']
        new_values = {'address': 'address4', 'price': 450004}
        response = requests.put(API_URL + RESOURCE + f"/{listing_id}", json = new_values)
        self.assertEqual(response.status_code, 200)
        res_obj = response.json()
        self.assertEqual(res_obj['address'], new_values['address'])
        self.assertEqual(res_obj['price'], new_values['price'])
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_delete(self):
        # POST a new item
        # Check status code
        # Get newly created item
        # DELETE item newly created item
        # GET item with id
        # Check if DELETE removed item
        # Check if 'Content-Type' header is correct
        new_listing = {'address': 'address4', 'price': 450004}
        response = requests.post(API_URL + RESOURCE, json=new_listing)
        res_obj = response.json()
        self.assertEqual(response.status_code, 201)
        listing_id = res_obj['id']
        response = requests.delete(API_URL + RESOURCE + f"/{listing_id}")
        self.assertEqual(response.status_code, 200)
        res_obj = response.json()
        listing_id = res_obj['id']
        response = requests.get(API_URL + RESOURCE + f"/{listing_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
