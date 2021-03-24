import requests
import json

class APIassignment():
    """Single suite to assert API response from reqres.in as per an assignment."""

    Base_URL = "https://reqres.in"

    reg_payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    login_payload = {
        "email" : "eve.holt@reqres.in"
    }

    def registerUser(self):
        url = APIassignment.Base_URL
        reg_response = requests.post(url + "/api/register", data= APIassignment.reg_payload)
        data = reg_response.json()
        print (data)
        return data['token']

    def loginUser(self):
        url = APIassignment.Base_URL
        login_response = requests.post(url + "/api/login", data = APIassignment.reg_payload)
        data = login_response.json()
        print (data['token'])
        return data['token']

    def deleteUser(self):
        url = APIassignment.Base_URL
        delete_response = requests.delete(url + "/api/users/2")
        data = delete_response.status_code
        return data

    def unknown(self):
        url = APIassignment.Base_URL
        ukn_response = requests.get(url + "/api/unknown")
        unknown_data = ukn_response.json()
        for i in range(len(unknown_data['data'])):
            if unknown_data['data'][i]['id'] == 2 and unknown_data['data'][i]['year'] == 2001:
                result = unknown_data['data'][i]
        print(result['id'] == 2 and result['year'] == 2001)
        return result

    def getUsers(self):
        url = APIassignment.Base_URL
        users_response = requests.get(url + "/api/users?page=2")
        userData = users_response.json()
        result = userData['data']
        print(result)
        return result

    def loginFail(self):
        url = APIassignment.Base_URL
        fail_response = requests.post(url + "/api/login", data = APIassignment.login_payload)
        response = fail_response.json()
        print(fail_response.status_code)
        return fail_response.status_code

    def searchJohn(self):
        url = APIassignment.Base_URL
        user_response = requests.get(url + "/api/users?page=2")
        result = user_response.json()
        first_names = [d['first_name'] for d in result['data']]
        return first_names


if "__name__" == "__main__":
    api = APIassignment()
    # api.


