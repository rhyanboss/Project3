"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask import render_template
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.route('/')
def me(name=None):
    """Return a friendly HTTP greeting."""
    return render_template('cards.html',name=name)