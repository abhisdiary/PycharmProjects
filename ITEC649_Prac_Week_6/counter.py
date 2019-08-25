from bottle import Bottle, template, request, response

app = Bottle()


@app.route('/')
def index():
    """Server the main application page"""

    if request.get_cookie('counter') is not None:
        counter = int(request.get_cookie('counter'))
        info = {
            'title': "Cookie Counter",
            'message': "You have been here " + str(counter) + " times"
        }
        response.set_cookie('counter', str(counter + 1))
    else:
        response.set_cookie('counter', '1')
        info = {
            'title': "Cookie Counter",
            'message': "Welcome this is your first visit"
        }

    return template('index', info)


if __name__ == '__main__':
    app.run()
