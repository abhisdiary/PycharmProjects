import random
from bottle import Bottle, template, static_file, request, response, redirect, HTTPError, abort
import model
import session

app = Bottle()


@app.route('/')
def index(db):
    """Render the index page"""
    session.get_or_create_session(db)
    products = model.product_list(db)
    count = len(products)
    info = {
        'title': 'The WT',
        'products': products,
        'number': count,
    }
    return template('index', info)


@app.route('/category/<cat>')
def categories(cat, db):
    """Generates Category Page"""
    session.get_or_create_session(db)
    if cat.lower() == 'men' or cat.lower() == 'women':
        product = {}
        temp = model.product_list(db, cat)
        cat_count = len(temp)
        if cat_count is not 0:
            product = model.product_list(db, cat)
            info = {
                'title': 'The WT',
                'products': product,
                'number': cat_count,
            }
    else:
        info = {
            'title': 'No products in this category',
            'number': 0
        }
    return template('index', info)


@app.route('/static/<filename:path>')
def static(filename, db):
    session.get_or_create_session(db)
    return static_file(filename=filename, root='static')


@app.route('/about')
def about(db):
    """Generates the about page"""
    session.get_or_create_session(db)
    info = {
        'title': "Welcome to WT! The innovative online store"
    }
    return template('about', info)


@app.route('/product/<id>')
def product_page(db, id):
    """Render the product page"""
    session.get_or_create_session(db)
    product = model.product_get(db, id)
    if product is not None:
        info = {
            'products': product,
            'number': 1,
        }
        return template('product', info)
    else:
        return HTTPError(status=404, body="404 Not Found")


@app.route('/cart', method="GET")
def cart_view(db):
    """Render the cart(GET) page"""
    session.get_or_create_session(db)
    cart = session.get_cart_contents(db)
    totalCost = 0
    for item in cart:
        totalCost += item['cost'] * item['quantity']
    cart = {
        'products': cart,
        'total': totalCost
    }
    return template('cart', cart)


@app.route('/cart', method="POST")
def cart_add(db):
    """Render the cart(POST) page"""
    cookieId = session.get_or_create_session(db)
    quantity = int(request.forms.get('quantity'))
    productId = request.forms.get('product')
    session.add_to_cart(db, productId, quantity)
    return redirect("/cart")


if __name__ == '__main__':
    from bottle.ext import sqlite
    from dbschema import DATABASE_NAME

    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
