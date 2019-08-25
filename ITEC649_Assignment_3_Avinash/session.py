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
    cur.execute("INSERT INTO sessions VALUES (?)", (key,))
    db.commit()

    response.set_cookie(COOKIE_NAME, key)

    return key


def get_or_create_session(db):
    """Get the current session either from a
    cookie in the current request or by creating a
    new session if none are present.

    If a new session is created, a cookie is set in the response.

    Returns the session key (string)
    """

    key = request.get_cookie(COOKIE_NAME)

    cur = db.cursor()
    cur.execute("SELECT key FROM sessions WHERE key=?", (key,))

    row = cur.fetchone()
    if not row:
        # no existing session so we create a new one
        key = new_session(db)

    return key


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""
    sql = "INSERT INTO cart (itemid, quantity) VALUES (?, ?)"
    cur = db.cursor()
    cur.execute(sql, (itemid, quantity, ))


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """
    items = []
    sql = """SELECT * from cart"""
    cur = db.cursor()
    cur.execute(sql)
    for item in cur.fetchall():
        items.append(item)

    # return the items in the cart
    return items
