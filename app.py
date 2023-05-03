import json

import requests

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                   headers={'accept': 'application/json'})

print(res.status_code)
print(res.json())

data = {
  "id": 0,
  "username": "hitheadman",
  "firstName": "vladimir",
  "lastName": "luzin",
  "email": "hitheadman@mail.ru",
  "password": "***",
  "phone": "string",
  "userStatus": 0
}

res1 = requests.post(f'https://petstore.swagger.io/v2/user',
                     headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                     data=json.dumps(data))

print(res1.status_code)
print(res1.json())

data = {
  "id": 0,
  "username": "chuvak",
  "firstName": "vladimir",
  "lastName": "luzin",
  "email": "hitheadman@mail.ru",
  "password": "***",
  "phone": "string",
  "userStatus": 0
}

res2 = requests.put(f'https://petstore.swagger.io/v2/user/hitheadman',
                     headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                     data=json.dumps(data))
print(res2.status_code)
print(res2.json())

res3 = requests.delete(f'https://petstore.swagger.io/v2/user/hitheadman', headers={'accept': 'application/json'})

print(res3.status_code)
print(res3.json())
