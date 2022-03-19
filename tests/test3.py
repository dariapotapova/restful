import requests
from flask import jsonify


user_data = jsonify({
                  'surname': 'a',
                  'name': 'b',
                  'age': 87,
                  'position': 'captain',
                  'speciality': None,
                  'address': None,
                  'email': 'po@inf.rr',
                  'hashed_password': None,
                  'modified_date': None,
                  'jobs': None})

response1 = requests.get("http://127.0.0.1:5000/api/v2/users")
response2 = requests.get("http://127.0.0.1:5000/api/v2/users/1")
response3 = requests.get("http://127.0.0.1:5000/api/v2/users/9282")
response4 = requests.post("http://127.0.0.1:5000/api/v2/users")
response5 = requests.delete("http://127.0.0.1:5000/api/v2/users/1")
response6 = requests.delete("http://127.0.0.1:5000/api/v2/users/9282")

print(response1.json(), response1.status_code)
print(response2.json(), response2.status_code)
print(response3.json(), response3.status_code)
print(response4.json(), response4.status_code)
print(response5.json(), response5.status_code)
print(response6.json(), response6.status_code)