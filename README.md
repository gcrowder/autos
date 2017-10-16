# Auto Mileage API

This is an actively developed RESTful API for recording gas usage, milage, and prices.

## Installation

- Clone this github repo (or download the source code)
- (optional) Use your favorite virtual environment tool to set up a new Python 3 environment. [Pipenv](https://docs.pipenv.org/) is the newest entry in that space, and is recommended by [Python.org](https://packaging.python.org/new-tutorials/installing-and-using-packages/)
- Install requirements: `pip install -r requirements` or `pipenv install`

## Running the API

### Create Tables
For development purposes, the API uses SQLite as its relational database. Before you run the API you must create the database tables. You do so by running:
`apistar create_tables`

### Launch the API

You launch the API by running:
`apistar run`

### Delete Tables

Should you desire to start from scratch (usually when running unit tests) you can drop the database tables with:
`apistar drop_tables`

### Unit Tests

Run the unit tests with:
`apistar test`

## The autos endpoint

The autos endpoint lets you create, get, update, and delete instances of the Auto model. The code for the Auto model is found in db.py. The views associated with the Auto model are found in routes.py

Method | URL | Example Request Body| Example Response
--- | --- | --- | ---
GET | `/autos/` | N/A | `[{"id": 1, "name": "Kid Hauler", "make": "Honda", "model": "Odyssey", "year": "2016"},{"id": 2, "name": "Commuter", "make": "Nissan","model": "Leaf", "year": "2013"}, {"id": 3, "name": "Weekend Roadster", "make": "Mazda", "model": "Miata", "year": "2017"}]`
POST | `/autos/` | `{"name": "Pickup", "make": "Ford", "model": "F150", "year": "2015"}` | `{"id":4, "name": "Pickup", "make": "Ford", "model": "F150", "year": "2015"}`
GET | `/autos/:id` | N/A | `{"id": 3, "name": "Weekend Roadster", "make": "Mazda", "model": "Miata", "year": "2017"}`
PATCH | `/autos/:id` | `{"year": "1998"}` | `{"id": 1, "name": "Kid Hauler", "make": "Honda", "model": "Odyssey", "year": "1998"}`
DELETE | `/autos/:id` | N/A | Status Code 204 No Response

## TODO

- Implement fuelstops views and endpoint
- Implement fuelstations views and endpoint
- (Stretch) Add maintenance model, views, and endpoint

## Intended use of API

A web app run on a mobile device, to log car fueling related data.