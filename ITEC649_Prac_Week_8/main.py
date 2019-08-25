import bottle
import model

app = bottle.Bottle()
bottle.debug(True)


@app.route('/')
def main(db):
    "Present the main page"

    return bottle.template('main.tpl')


@app.post('/')
def handle_form(db):
    """Handle post from submission"""


if __name__ == "__main__":
    from bottle.ext import sqlite

    # install the database plugin
    app.install(sqlite.Plugin(dbfile=model.DATABASE_NAME))

    app.run(port=8011)
