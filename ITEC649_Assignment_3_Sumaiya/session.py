"""
Code for handling sessions in our web application
"""

from bottle import request, response
import uuid
import json

import model
import dbschema

COOKIE_NAME = 'session'


def get_or_create_session(db):
    """Get the current sessionid either from a
    cookie in the current request or by creating a
    new session if none are present.

    If a new session is created, a cookie is set in the response.

    Returns the session key (string)
    """

    cookie = request.get_cookie(COOKIE_NAME)

    cur = db.cursor()
    sql = """SELECT sessionid FROM sessions WHERE sessionid=?"""
    cur.execute(sql, (cookie,))

    row = cur.fetchone()
    # Check if session exists or not
    if not row:
        cookie = str(uuid.uuid4())
        cur = db.cursor()
        sql = """INSERT INTO sessions(sessionid) VALUES (?)"""
        cur.execute(sql, (cookie,))
        db.commit()
        response.set_cookie(COOKIE_NAME, cookie, path="/")
    return cookie


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""
    key = get_or_create_session(db)
    product= model.product_get(db,itemid)
    item = {
        'id': itemid,
        'quantity': quantity,
        'name': product[1],
        'cost': float(product[5])*float(quantity),
    }
    cart = get_cart_contents(db)
    #Check if cart empty for the session
    if cart == []:
        cart.append(item)
    else:
        for each in cart:
            if itemid == each['id']:
                each['quantity'] = each['quantity'] + quantity
            else:
                cart.append(item)
                break
    data = json.dumps(cart)
    sql = """UPDATE sessions
             SET data='%s'
             WHERE sessionid=?""" % (data)
    cur = db.cursor()
    cur.execute(sql, (key,))


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """
    key = get_or_create_session(db)
    sql = """SELECT data FROM sessions WHERE sessionid=?"""
    cur = db.cursor()
    cur.execute(sql, (key,))
    row = cur.fetchone()
    if row['data'] is None:
        cart = []
    else:
        cart = json.loads(row['data'])
    return cart
