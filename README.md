# demo-flask-api

This repository serves only to experiment [Flask](http://flask.pocoo.org) to build a REST API

### Running

Inside the root of the repository:
```
> set FLASK_APP=all_apis.py
> flask run
```
This will run locally in this endpoint: http://127.0.0.1:5000

### Testing

I tested GETs in a browser. To test POST I used [POSTMAN](https://www.getpostman.com/)

**GET /employees**

- Response data (with initial data):

```
{
  "employees": {
    "employee": [
      {
        "lastName": "Santos",
        "id": "1",
        "firstName": "Filipa"
      },
      {
        "lastName": "Sousa",
        "id": "2",
        "firstName": "Maria"
      },
      {
        "lastName": "Oliveira",
        "id": "3",
        "firstName": "Teresa"
      }
    ]
  }
}
```

**POST /employee**

- Request data (with new employee):
```
{
  "lastName": "Bonita",
  "id": "4",
  "firstName": "Isla"
}
```

- Response data (with all employees):
```
{
  "employees": {
    "employee": [
      {
        "firstName": "Filipa",
        "id": "1",
        "lastName": "Santos"
      },
      {
        "firstName": "Maria",
        "id": "2",
        "lastName": "Sousa"
      },
      {
        "firstName": "Teresa",
        "id": "3",
        "lastName": "Oliveira"
      },
      {
        "firstName": "Isla",
        "id": "4",
        "lastName": "Bonita"
      }
    ]
  }
}
```

- Terminal Output:

```
demo-flask-api>flask run
 * Serving Flask app "all_apis"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [21/Mar/2018 22:44:19] "GET /employees HTTP/1.1" 200 -
127.0.0.1 - - [21/Mar/2018 22:44:24] "POST /employee HTTP/1.1" 200 -
127.0.0.1 - - [21/Mar/2018 22:44:31] "GET /employees HTTP/1.1" 200 -
127.0.0.1 - - [21/Mar/2018 22:45:00] "POST /employee HTTP/1.1" 200 -
127.0.0.1 - - [21/Mar/2018 22:45:06] "GET /employees HTTP/1.1" 200 -
```
