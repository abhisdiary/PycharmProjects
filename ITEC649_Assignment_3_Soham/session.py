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
    curs = db.cursor()
    cookie = request.get_cookie(COOKIE_NAME)
    query = """SELECT sessionid FROM sessions WHERE sessionid=?"""
    curs.execute(query, (cookie,))
    dbData = curs.fetchone()

    if dbData:
        return cookie
    else:
        sessionId = create_new_session(db)
        response.set_cookie(COOKIE_NAME, sessionId)
        return sessionId


def create_new_session(db):
    curs = db.cursor()
    sessionId = str(uuid.uuid4())
    sql = """INSERT INTO sessions(sessionid) VALUES (?)"""
    curs.execute(sql, (sessionId,))
    db.commit()
    return sessionId


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""
    product = model.product_get(db, itemid)
    cart = get_cart_contents(db)
    if len(cart) != 0:
        for each_item in cart:
            if each_item['id'] == itemid:
                each_item['quantity'] = each_item['quantity'] + quantity
            else:
                item = {
                    'id': itemid,
                    'quantity': quantity,
                    'name': product['name'],
                    'cost': float(product['unit_cost']) * quantity
                }
                cart.append(item)
                break
    else:
        item = {
            'id': itemid,
            'quantity': quantity,
            'name': product['name'],
            'cost': float(product['unit_cost']) * quantity
        }
        cart.append(item)
    data = json.dumps(cart)
    curs = db.cursor()
    sessionId = get_or_create_session(db)
    query = """UPDATE sessions SET data=? WHERE sessionid=?"""
    curs.execute(query, (data, sessionId))
    db.commit()


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """
    curs = db.cursor()
    sessionId = get_or_create_session(db)
    query = """SELECT data FROM sessions WHERE sessionid=?"""
    curs.execute(query, (sessionId,))
    row = curs.fetchone()
    cartData = []
    if row['data'] is not None:
        cartData = json.loads(row['data'])
    return cartData
