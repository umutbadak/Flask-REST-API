# RESTful CRUD API
 A simple RESTful CRUD API application using Flask, SQLAlchemy, Flask-Restful library and Sqlite database.
 
## Installation 
* Get the source code of the project by cloning the project repository

```
$ git clone https://github.com/umutbadak/Flask-REST-API.git
$ cd Flask-REST-API
```

* Install virtualenv using pip
```
$ pip install virtualenv 
```
* Create virtual environment for the project
```
$ virtualenv .venv 
```  
* Activate virtual environment
```
$ source .venv/bin/activate
```  
 * Install dependencies
```
$ pip install -r requirements.txt
``` 
## Running The Application
* Create database 
```
$ python init_db.py
``` 
* Populate database 
```
$ python populate_db.py
``` 
* Run the app 
```
$ python app.py
```
Application will run on following URL: <br>
http://127.0.0.1:5000/api/v1

* Testing app
```
$ python -m unittest -v test.py
```
Note that running test script will delete database tables. 
After running test script,  run init_db.py to re-create database tables.

## API Documentation

#### 1- Create A Listing

**Request**
```
POST /listings
```
**Parameters**

Name|Type|Required
:-:|:-:|:-:
`address`|`string`|`True`
`price`|`integer`|`True`


**Request Body**
```
{
    "address": "125 Parkway Dr", 
    "price":422000
}
```

**Response**

```
{
    "id" : 1
    "address": "125 Parkway Dr", 
    "price":422000
}
```

**Status Codes** 

Success : 201 

#### 2- List All Listings

**Request**
```
GET /listings
```

**Response**

```
[
    {
        "id": 1,
        "address": "301 Mullholand Dr.",
        "price": 356000
    },
    {
        "id": 2,
        "address": "10 Park Av.",
        "price": 430000
    }
]
```

**Status Codes** 

Success : 200
 
#### 3- Listing Detail 

**Request**
```
GET /listings/:id
```

**Response**

```
    {
        "id": 2,
        "address": "10 Park Av.",
        "price": 430000
    }
```

**Status Codes** 

Success : 200 <br>
Error (Listing does not exist) : 404

#### 4- Update Listing 

**Request**
```
PUT /listings/:id
```

**Parameters**

Name|Type|Required
:-:|:-:|:-:
`address`|`string`|`True`
`price`|`integer`|`True`

**Response**

```
    {
        "id": 2,
        "address": "10 Park Av.",
        "price": 430000
    }
```

**Status Codes** 

Success : 200 <br>
Not found: 404

#### 5- Delete Listing 

**Request**
```
DELETE /listings/:id
```

**Response**

```
    {
        "id": 2,
        "address": "10 Park Av.",
        "price": 430000
    }
```

**Status Codes** 

Success : 200 <br>
Error (Listing does not exist) : 404

