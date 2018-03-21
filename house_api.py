from base_api import *


@app.route("/home")
def get_home():
    home = """{"message": "Hello Home!", "rooms": ["bedroom", "kitchen", "bathroom"], "occupied": 1,
            "number_of_occupants": 4, "occupants": {"friend0": "Lily", "friend1": "Jonh", "friend2": "Mary"},
            "random_string": "Hello World!!!"}"""

    return home


@app.route("/school")
def get_school():
    return "Hello School!"
