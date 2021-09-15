# API Documentation
To Deploy the API to the server use SSH to copy the API.py file into the `/var/www/html/flaskapi/` folder (API.wsgi must be present in the flaskapi folder with API.py). Next run the command: `systemctl reload apache2` which will restart the server and the new API.

## Endpoints (Routes)
### Login
- url: `/api/login/<usr>/<pwd>`
- parameters: username (string) and password (string)
- return: A json object of the following form...

```
{
    "response": 
        {
            "code": 200, 
            "message": "Login success", 
            "data": [User ID, First Name, Last Name]
        }
}
```
*Note: The data key will be missing if login fails and an appropriate code and message will be displayed*
### Register
- url: `/api/register/<fname>/<lname>/<usr>/<pwd>`
- parameters: first name (string), last name (string), username (string), and password (string)
- return: A json object with error code 200 for success. Any other number is a failure...
```
{
    "response": 
        {
            "code": 200, 
            "message": "Register success"
        }
}
```
### Delete User
- url: `/api/deleteuser/<userid>`
- parameters: User's ID (int)
- return A json object with a 200 error code for success and 404 for failure
### Add Contact
- url: `/api/addcontact/<fname>/<lname>/<phonenum>/<emailadd>/<userid>`
- parameters: First Name (string), Last Name (string), Phone Number (string), Email Address (string), and the User's ID 
  who has this contact (int)
  
- return: A json object with error code 200 for success, 401 if the contact already exists, and 404 for connection failures
### Delete Contact
- url: `/api/deletecontact/<identifier>`
- parameters: The contact's identifier number (int)
- return: A json object with error code 200 for success or 404 for connection failures
### Edit Contact
- url: `/api/editcontact/<fname>/<lname>/<phonenum>/<emailadd>/<identifier>`
- parameters: The First Name (string), Last Name (string), Phone Number (string), Email Address (string), and User ID of
the user who owns the contact (int)
  
- return: A json object with error code 200 for success or 404 for connection failures
### Search Contacts
- url: `/api/searchcontacts/<name>/<userid>`
- parameters: The Name (string), and User ID of the currently logged in user (int)
- return: A json object with error code 200 if the search was successful and 404 if there was a connection failure.
 There will also be a data key that maps to an array of arrays, where each sub-array has all the contact information for
  each of the contacts that matched the search query
  
```
{
    "response": 
        {
            "code": 200, 
            "message": "Contact search success", 
            "data": [[Contact's ID, Date Created, First Name, Last Name, E-Mail, Phone Number, Associated User ID], [...]]
        }
}
```