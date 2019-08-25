# a simple chat application that is susceptible to XSS attacks
# Author: Steve Cassidy
# there are at least two vulnerabilities in this script that allow
# a user to inject Javascript code into pages
#  -- find them and demonstrate an exploit
#  -- fix them
#
# Ref: https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet
#

from database import COMP249Db

from bottle import Bottle, request, response, template

import re

app = Bottle()


def create_table(db):
    """Create database table for the messages application
    given a database connection 'db'.
    Removes any existing data that might be in the
    database."""

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS messages")
    cursor.execute("""
    CREATE TABLE messages (
       message text
    )
    """)


def quote_and_clean(message):
    """Process a message so that it is safe to insert in
    the page. Some HTML is allowed but we want to avoid javascript
    attacks so we remove the <script> tag. Convert #tags to
    links."""

    # find and remove any script tags that might have javascript
    message = message.replace('<script>', '--script--')
    message = message.replace('<body', '--script--')
    message = re.sub('<[^<]+?>', '--script--', message)

    # don't allow javascript in attributes
    message = message.replace('javascript:', '--REPLACED--')

    # replace tags with links
    (message, count) = re.subn(r'#(\w+)', r'<a href="/tag/\1">#\1</a>', message)

    return message


def store_message(db, message):
    """Store a new message in the database"""

    message = quote_and_clean(message)
    cursor = db.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES (?)", (message,))
    db.commit()


def get_messages(db):
    """Return a list of messages from the database"""

    cursor = db.cursor()
    cursor.execute("SELECT message FROM messages")
    result = []
    for row in cursor:
        result.append(row[0])
    return result


def get_tag_messages(db, tag):
    """Return a list of messages from the database containing the given tag"""

    cursor = db.cursor()
    # find messages containing the text #tag
    cursor.execute("SELECT message FROM messages WHERE message like ?", ('%#' + tag + '%',))
    result = []
    for row in cursor:
        result.append(row[0])
    return result


# --------------------- routes ---------------------------

@app.route('/')
def index():
    """Home page"""

    db = COMP249Db()

    info = dict()
    info['title'] = 'Have a Conversation'
    # get the list of messages from the database
    info['messages'] = get_messages(db)

    return template('default.tpl', info)


@app.post('/messages')
def post_message():
    """Process like form post request"""

    # get the form field
    message = request.forms.get('message')

    if message:
        store_message(db, message)

    response.set_header('Location', '/')
    response.status = 303

    return 'Redirect to /'


@app.route('/tag/<tag:path>')
def tags(tag):
    """Return a page of messages containing the given tag"""

    db = COMP249Db()

    info = dict()
    info['title'] = 'Messages with tag <em>#' + tag + "</em>"
    # get the list of messages from the database
    info['messages'] = get_tag_messages(db, tag)

    return template('default.tpl', info)


if __name__ == "__main__":
    db = COMP249Db()
    create_table(db)
    app.run()
