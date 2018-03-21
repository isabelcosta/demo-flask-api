from base_api import *


@app.route("/employees")
def get_employees():
    employees_json = json.load(open('employees.json'))
    return json.dumps(employees_json, indent=2)
