from base_api import *


@app.route("/")
def get_hello():
    return "Hello World!"
