import requests

url = "https://joseojedak16992.api-us1.com/api/3/contacts"

payload = {"contact": {
        "email": "test9@example.com",
        "firstName": "test9",
        "lastName": "test0",
        "phone": "7223224241",
        # "fieldValues": [
        #     {
        #         "field": "1",
        #         "value": "The Value for First Field"
        #     },
        #     {
        #         "field": "6",
        #         "value": "2008-01-20"
        #     }
        # ]
    }}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    'Api-Token': "64dcb7f53fb7fe6035351e6acccb2dd788cd161cadf8a2ba910791c2f6453b52e2173152"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)