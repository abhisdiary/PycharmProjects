"""
Code for handling sessions in our web application
"""

from bottle import request, response
import uuid
import json

import model
import dbschema

COOKIE_NAME = 'session'


def new_session(db):
    """Make a new session key, store it in the db.
    Add a cookie to the response with the session key and
    return the new session key"""

    # use the uuid library to make the random key
    key = str(uuid.uuid4())
    cur = db.cursor()
    # store this new session key in the database with no likes in the value
    cur.execute("INSERT INTO sessions(sessionid) VALUES (?)", (key,))
    db.commit()

    response.set_cookie(COOKIE_NAME, key)

    return key


def get_or_create_session(db):
    """Get the current sessionid either from a
    cookie in the current request or by creating a
    new session if none are present.

    If a new session is created, a cookie is set in the response.

    Returns the session key (string)
    """
    sessionid = request.get_cookie(COOKIE_NAME)

    cur = db.cursor()
    cur.execute("SELECT sessionid FROM sessions WHERE sessionid=?", (sessionid,))

    row = cur.fetchone()
    if not row:
        # no existing session so we create a new one

        sessionid = new_session(db)

    return sessionid


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""
    cursor = db.cursor()
    item = dict(model.product_get(db, itemid))
    cart = get_cart_contents(db)
    if len(cart) is not 0 and any(item.get('id', None) == int(itemid) for item in cart):
        for item in cart:
            if int(itemid) == int(item["id"]):
                item["quantity"] = float(item["quantity"]) + float(quantity)
                item["cost"] = float(quantity) * item["unit_cost"]
    else:
        item["quantity"] = float(quantity)
        item["cost"] = float(quantity) * item["unit_cost"]
        cart.append(item.copy())
    data = json.dumps(cart)
    cursor.execute("UPDATE sessions set data=? WHERE sessionid=? ", (data, request.get_cookie(COOKIE_NAME)))
    db.commit()


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """
    cursor = db.cursor()
    cursor.execute("SELECT data FROM sessions WHERE sessionid=?", (request.get_cookie(COOKIE_NAME),))
    row = cursor.fetchone()
    cart = []
    if row['data'] is not None:
        cart = json.loads(row['data'])
    return cart
