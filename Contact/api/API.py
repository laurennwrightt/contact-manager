import mysql.connector
import flask
from flask import request, jsonify


# All API endpoints (Otherwise known as routes) are a set of functions that will perform some behaviour, and return a
# response. The way that flask works is it creates an indefinitely running application that allows any function marked
# with @app.route() to be called through a URL. To Deploy the API, log into the server, navigate to the /var/www/api
# folder and copy and paste this file into there. To run it simply enter `python3 API.py`

# Create a connection to the database and a cursor that we use to perform database operations


# the string inside @api.route() is what will come after `165.227.185.106:5000` in the url
api = flask.Flask(__name__)

def connect_to_database():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="TheBeast",
        password="WeLoveCOP4331",
        database="COP4331"
    )
    cursor = connection.cursor()
    return (connection, cursor)


def unpack_results(stored_results):
    results = []
    for result in stored_results:
        results = results + result.fetchall()
    return results


@api.route('/ping')
def ping():
    return jsonify({"response": {"code": 200, "message": "Ping!"}})


@api.route('/login/<usr>/<pwd>', methods=['POST'])
def login(usr, pwd):
    try:
        connection, cursor = connect_to_database();
        cursor.callproc('Login', (usr, pwd))
        results = unpack_results(cursor.stored_results())
        connection.commit()
        response = {}
        if len(results) == 0:
            response.update({"response": {"code": 401, "message": "Failed login with credentials"}})
        else:
            user = results[0]
            response.update({"response": {"code": 200, "message": "Login success", "data": [user[0], user[3], user[4]]}})
        cursor.close()
        connection.close()
        return jsonify(response)
    except Exception as ex:
        cursor.close()
        connection.close()
        print(ex)
        return jsonify({"response": {"code": 404, "message": f"Database connection failed\n{ex}"}})


@api.route('/register/<fname>/<lname>/<usr>/<pwd>', methods=['POST'])
def register(fname, lname, usr, pwd):
    try:
        connection, cursor = connect_to_database();
        cursor.callproc('Register', (fname, lname, usr, pwd))
        results = unpack_results(cursor.stored_results())
        connection.commit()
        response = {}
        if len(results) == 0:
            response.update({"response": {"code": 401, "message": "User already exists"}})
        else:
            response.update({"response": {"code": 200, "message": "Register success"}})
        cursor.close()
        connection.close()
        return jsonify(response)
    except Exception as ex:
        cursor.close()
        connection.close()
        print(ex)
        return jsonify({"response": {"code": 404, "message": "Database connection failed"}})


@api.route('/deleteuser/<userid>', methods=['POST'])
def deleteuser(userid):
    try:
        connection, cursor = connect_to_database();
        cursor.callproc('DeleteUser', (userid))
        unpack_results(cursor.stored_results())
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"response": {"code": 200, "message": "User successfully deleted"}})
    except Exception as ex:
        cursor.close()
        connection.close()
        print(ex)
        return jsonify({"response": {"code": 404, "message": "Database connection failed"}})


@api.route('/addcontact/<fname>/<lname>/<phonenum>/<emailadd>/<userid>', methods=['POST'])
def addcontact(fname, lname, phonenum, emailadd, userid):
    try:
        connection, cursor = connect_to_database();
        cursor.callproc('AddContact', (fname, lname, phonenum, emailadd, userid))
        results = unpack_results(cursor.stored_results())
        connection.commit()
        response = {}
        if len(results) == 0:
            response.update({"response": {"code": 401, "message": "Contact already exists"}})
        else:
            response.update({"response": {"code": 200, "message": "Contact add success"}})
        cursor.close()
        connection.close()
        return jsonify(response)
    except Exception as ex:
        cursor.close()
        connection.close()
        print(ex)
        return jsonify({"response": {"code": 404, "message": f"Database connection failed\n{ex}"}})


@api.route('/deletecontact/<identifier>', methods=['POST'])
def deletecontact(identifier):
    try:
        connection, cursor = connect_to_database();
        cursor.callproc('DeleteContact', (identifier,))
        unpack_results(cursor.stored_results())
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"response": {"code": 200, "message": "Contact delete success"}})
    except Exception as ex:
        cursor.close()
        connection.close()
        print(ex)
        return jsonify({"response": {"code": 404, "message": f"{ex}"}})


@api.route('/editcontact/<fname>/<lname>/<phonenum>/<emailadd>/<identifier>', methods=['POST'])
def editcontact(fname, lname, phonenum, emailadd, identifier):
    try:
        connection, cursor = connect_to_database();
        cursor.callproc("EditContact", (fname, lname, phonenum, emailadd, identifier))
        unpack_results(cursor.stored_results())
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"response": {"code": 200, "message": "Contact edit success"}})
    except Exception as ex:
        cursor.close()
        connection.close()
        print(ex)
        return jsonify({"response": {"code": 404, "message": f"Database connection failed\n{ex}"}})


@api.route('/searchcontacts/<name>/<userid>', methods=['GET'])
def searchcontacts(name, userid):
    try:
        connection, cursor = connect_to_database();
        if name == '_':
            name = ''
        cursor.callproc("SearchContacts", (name, userid))
        results = unpack_results(cursor.stored_results())
        response = {"response": {"code": 200, "message": "Contact search success", "data": results}}
        cursor.close()
        connection.close()
        return jsonify(response)
    except Exception as ex:
        cursor.close()
        connection.close()
        print(ex)
        return jsonify({"response": {"code": 404, "message": f"Database connection failed\n{ex}"}})


# Start the API
if __name__ == '__main__':
    api.run(host='0.0.0.0')