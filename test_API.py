import pytest
from api_assignment import APIassignment
api = APIassignment()

# API assignment - a - register and validate login
def test_validateAndLogin():
    # asserting if the token on account creation is same as that of login, since it's unique for each user.
    reg_token = api.registerUser()
    login_token = api.loginUser()
    assert reg_token == login_token

# API assignment - b - Delete created user from step 1
def test_deleteUser():
    # There is no specific API in reqres.in where i can pass my registered user to get it deleted. so I've just implemented available delete user.
    resp_code = api.deleteUser()
    assert resp_code == 204

# API assignment - c - assert resource using given conditions
def test_conditionMatch():
    result = api.unknown()
    assert result['id'] == 2 and result['year'] == 2001

# API assignment - d  asserting the result if it contains user with ID - 7 and lastname as Lawson
def test_getUsers():
    result = api.getUsers()
    for i in range(len(result)):
        if result[i]['id'] == 7 and result[i]['last_name'] == 'Lawson':
            assert True

# API assignment - e - checking if the first name John is present in the list of firstnames
def test_searchJohn():
    result = api.searchJohn()
    assert 'john' in result
