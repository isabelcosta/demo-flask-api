from base_api import *

employees_json = json.load(open('employees.json'))


@app.route("/employees")
def get_employees():
    return json.dumps(employees_json, indent=2)


@app.route('/employee', methods=['POST'])
def post_employee():

    # Get json request data
    receiveddata = request.data
    dataDict = json.loads(receiveddata)

    # Get each element of the request data
    req_first_name = dataDict['firstName']
    req_last_name = dataDict['lastName']
    req_id = dataDict['id']

    # Creating json object
    newData = {}
    newData['firstName'] = req_first_name
    newData['lastName'] = req_last_name
    newData['id'] = req_id

    employees_json['employees']['employee'].append(newData)

    return jsonify(employees_json)
