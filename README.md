# test_Rest_API
simple Rest API testing using requests and pytest. Rest APIs from the website reqres.in 
Assignment are as follows
  a) Test the Register API by registering the user successfully using https://reqres.in/api/register and by logging in using the data used for the registration on API        https://reqres.in/api/login. Pass it only if the user is created and able to login
  b) Using details of the user created in step a,  Delete the user registered above and assert an unsuccessful login attempt on login API https://reqres.in/api/login. Pass it only   if the user created in Step a is deleted and unable to login
  c) Assert a resource on https://reqres.in/api/unknown where page=1 and ID=2, year=2001
  d) Assert a user on https://reqres.in/api/users?page=2 where the assertion is passed if the payload contains user with ID=7, Lastname =Lawson
  e) Assert the payload in API https://reqres.in/api/users/2 where it will check for first_name as "John" and fails the test if it's not "John"
