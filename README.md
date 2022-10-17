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
* Create database script
```
$ python init_db.py
``` 
* Populate database script
```
$ python populate_db.py
``` 
* Run the app 
```
$ python app.py
```
Application will run on following URL http://127.0.0.1:5000/api/v1

* Testing app
```
$ python -m unittest -v test.py
```
Note that running test script will delete database tables. After running test script,  run init_db.py again to re-create database tables.

## API Documentation

#### 1- Create Listing
Creates a single listing and returns created listing with id.
* ##### URL #####
    /listings
* ##### Method ##### 
    ```POST```
* ##### URL Params ##### 
    None
* ##### Data Params ##### 
    ```
    address = [string]
    price = [integer]
    ```
**Parameters**

Name|Type|Description|Required
:-:|:-:|:-:|:-:
`name`|`string`|category name|`True`
`short_desc`|`string`|category short description|`False`

* ##### Method ##### 
* ##### Method #####     
* Url Params
-
* Data Params

**Request**
```
POST /listings
```
**Parameters**

| Name          | Type          | Required  |
| ------------- | ------------- | --------- |
| address       | string        | True      |
| price         | integer       | True      |

** Request Body **
```
{
    "address": "address1", 
    "price":"122"
}
```
** Response **