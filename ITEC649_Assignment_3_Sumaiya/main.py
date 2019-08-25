import random
from bottle import Bottle, template, static_file, request, response, redirect, HTTPError, abort
import model
import session

app = Bottle()


@app.route('/')
def index(db):
    """Render the index page"""

    session.get_or_create_session(db)
    # fetch all product
    cursor = db.cursor()
    cursor.execute('SELECT name from products')
    rows = cursor.fetchall()
    count = len(rows)
    product = {}
    # initalize empty data
    for no in range(count):
        product[no] = []
    for no in range(count):
        product[no].append(model.product_get(db, no))
    info = {
        'title': 'The WT',
        'products': product,
        'number': count,
    }
    return template('index', info)


@app.route('/category/:cat')
def filter(cat, db):
    """Render the category page"""
    session.get_or_create_session(db)
    product = {}
    temp = model.product_list(db, cat)
    cat_count = len(temp)
    if cat_count is not 0:
        # for i in range(cat_count):
        #     product[i] = []
        for i in range(cat_count):
            product[i] = [temp[i]]
        if product is not None:
            info = {
                'title': 'The WT',
                'products': product,
                'number': cat_count,
            }
            return template('index', info)
        else:
            info = {
                'title': "No products in this category",
                'products': product,
                'number': cat_count,
            }
            return template('index', info)


@app.route('/static/<filename:path>')
def static(filename, db):
    session.get_or_create_session(db)
    return static_file(filename=filename, root='static')


@app.route('/about')
def about(db):
    """Render the about page"""
    session.get_or_create_session(db)
    return template('about')


@app.route('/product/:id')
def product_page(db, id):
    """Render the product page"""
    session.get_or_create_session(db)
    prod = model.product_get(db, id)
    if prod is None:
        abort(404)
    else:
        info = {
            'products': prod,
            'number': 1,
        }
        return template('product', info)


@app.route('/cart', method="GET")
def cart_view(db):
    """Render the cart(GET) page"""
    session.get_or_create_session(db)
    current = session.get_cart_contents(db)
    cost = 0
    for each in current:
        cost += each['cost'] * each['quantity']
    cart = {
        'content': current,
        'total': cost,
    }
    return template('cart', cart)


@app.route('/cart', method="POST")
def cart_add(db):
    """Render the cart(POST) page"""

    key = session.get_or_create_session(db)

    quantity = int(request.forms.get('quantity'))
    product = request.forms.get('product')

    session.add_to_cart(db, product, quantity)
    current = session.get_cart_contents(db)
    cost = 0
    for each in current:
        cost += each['cost'] * each['quantity']
    cart = {
        'content': current,
        'total': cost,
    }
    return redirect("/cart")


if __name__ == '__main__':
    from bottle.ext import sqlite
    from dbschema import DATABASE_NAME

    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
