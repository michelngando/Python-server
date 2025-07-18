from flask import Flask, request
from data import catalog
import json


app = Flask("Server") #Creating the server

#Creating the endpoints
@app.get("/")  #This is called a decorator
def home():
    return "Hello from Python"

@app.get("/test")
def test():
    return "This is a test page"

@app.get("/about")
def about():
    return "<h1>Michel Ngando</h1>"

@app.get("/api/about")
def about_me():
    me = {
        "name": "Michel",
        "last": "Ngando",
        "email": "mngando@thisclass.com"
    }
    return me   

@app.get("/api/products")
def get_products():
    return json.dumps(catalog) #python to json --> #json.parse: json to python

@app.post("/api/products")
def save_products():
    data = request.get_json()
    catalog.append(data) #add the product to the catalog
    return json.dumps(data)


@app.get("/api/products/count")
def products_number():
    #nbr_of_products = len(catalog)
    return f"We have {len(catalog)} products" #Or return json.dumps(nbr_of_products)
    























app.run(debug=True, port=8000)