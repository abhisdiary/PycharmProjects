
import random
from bottle import Bottle, template, static_file, request,response , redirect, HTTPError

import model
import session

app = Bottle()


@app.route('/')
def index(db):
    session.get_or_create_session(db)
    products = model.product_list(db)

    info = {
        'title': "The WT Store",
        "products": products
    }

    return template('index', info)


@app.route('/about')
def about(db):
    session.get_or_create_session(db)
    info = {
        'title': "The WT Store",
        "body": "Welcome to WT! The innovative online store"
    }

    return template('about', info)


@app.route('/category/<cat>')
def category(db, cat):
    session.get_or_create_session(db)
    if cat == "men" or cat == "women":
        products = model.product_list(db, category=cat)
    else:
        products = "No products in this category"

    info = {
        'products': products
    }

    return template('category', info)


@app.route('/product/<id>')
def product(db, id):
    session.get_or_create_session(db)
    product = model.product_get(db, id=id)
    if product is None:
        return HTTPError(status=404, body="404 Not Found")
    info = {
        'product': product
    }
    session.response.set_cookie('new_cookie','dummy', path="/")
    return template('products', info)


@app.route('/cart', method=['GET'])
def cart(db):
    session.get_or_create_session(db)
    cart = session.get_cart_contents(db)
    total_cost = 0
    if len(cart) is 0:
        cart = "Your Cart is Empty"
    else:
        for item in cart:
            total_cost = total_cost+item["cost"]
    info = {
        "title": "CART",
        "cart": cart,
        "total_cost": total_cost
    }


    return template('cart', info)


@app.route('/cart', method=['POST'])
def form_handler(db):
    session.get_or_create_session(db)
    quantity = request.forms.get('quantity')
    item_id = request.forms.get('product')
    session.add_to_cart(db, itemid=item_id, quantity=quantity)
    redirect('/cart')

@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


if __name__ == '__main__':

    from bottle.ext import sqlite
    from dbschema import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
