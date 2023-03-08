# Question – Using Python v3.0:
## Test get users API
Host: https://reqres.in
Path: /api/users
Parameter: page
Method: GET

Target API:
https://reqres.in/api/users?page=1
Response:
{"page":1,"per_page":3,"total":12,"total_pages":4,"data":
[{"id":1,"first_name":"George","last_name":"Bluth","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"},
{"id":2,"first_name":"Janet","last_name":"Weaver","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"},
{"id":3,"first_name":"Emma","last_name":"Wong","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg"}]}

This is an API that would return a list of user data in JSON format
We can see the output as above. There are total 12 user data and all data are in 2 pages. Each page has 6 data
You can use parameter "page" to specify the page of data

Please use Python to write a function that given two numbers and return a list of the name(first_name + last_name) of the users whose ID is between this two numbers
The result name list should be sorted according to the first name
And then design the test cases to verify your functions 

e.g.
assert get_user_full_name_list (1, 3) == ['Emma Wong', 'George Bluth', 'Janet Weaver']
assert get_user_full_name_list (5, 8) == ['Charles Morris', 'Emma Wong', 'Eve Holt', 'Janet Weaver']

Note:
1. You NEED to set the header User-Agent to ""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
so that you can get the data correctly.
2. Both two input parameters should be integer. For any invalid input, return an empty list

