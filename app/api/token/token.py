# pip3 install requests
import requests
import json

API_KEY_SECRET = "bytepixelsfu_default_secret"
bytepixel_URL = "https://sfu.bytepixel.com/api/v1/token"
#bytepixel_URL = "http://localhost:3010/api/v1/token"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

data = {
    "username": "username",
    "password": "password",
    "presenter": "true",
    "expire": "1h"
}

response = requests.post(
    bytepixel_URL, 
    headers=headers, 
    json=data
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("token:", data["token"])
