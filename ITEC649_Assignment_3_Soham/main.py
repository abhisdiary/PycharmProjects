from bottle import Bottle, template, static_file

app = Bottle()


@app.route('/')
def index(db):

    info = {
        'title': "The WT Store",
    }

    return template('index', info)


@app.route('/product')
def product(db):

    return template('product')


@app.route('/cart')
def cart(db):

    return template('cart')


@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


if __name__ == '__main__':

    from bottle.ext import sqlite
    from dbschema import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
