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
    """Get the current sessionid either from a cookie in the current request or by creating a
    new session if none are present. If a new session is created, a cookie is set in the response. Returns the session key (string)
    """
    cookieId = request.get_cookie(COOKIE_NAME)
    cur1 = db.cursor()
    cur1.execute("SELECT sessionid FROM sessions WHERE sessionid=?", (cookieId,))
    row = cur1.fetchone()
    if row:
        return cookieId
    else:
        cookieId = str(uuid.uuid4())
        cur2 = db.cursor()
        cur2.execute("""INSERT INTO sessions(sessionid) VALUES (?)""", (cookieId,))
        db.commit()
        response.set_cookie(COOKIE_NAME, cookieId, path="/")
        return cookieId


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""
    cur = db.cursor()
    key = get_or_create_session(db)
    product = model.product_get(db, itemid)
    item = {
        'id': itemid,
        'quantity': quantity,
        'name': product['name'],
        'cost': float(product['unit_cost']) * float(quantity),
    }
    cart = get_cart_contents(db)
    if len(cart) is not 0:
        for item in cart:
            if int(itemid) == int(item['id']):
                item['quantity'] = int(item['quantity']) + int(quantity)
            else:
                cart.append(item)
                break
    else:
        cart.append(item)
    data = json.dumps(cart)
    cur.execute("""UPDATE sessions SET data=? WHERE sessionid=?""", (data, key))
    db.commit()


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """
    cart = []
    cur = db.cursor()
    cur.execute("""SELECT data FROM sessions WHERE sessionid=?""", (get_or_create_session(db),))
    row = cur.fetchone()
    if row['data'] is not None:
        cart = json.loads(row['data'])
    return cart
