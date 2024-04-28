# pip3 install requests
import requests
import json

API_KEY_SECRET = "bytepixelsfu_default_secret"
bytepixel_URL = "https://sfu.bytepixel.com/api/v1/meeting"
# bytepixel_URL = "http://localhost:3010/api/v1/meeting"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

response = requests.post(
    bytepixel_URL,
    headers=headers
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("meeting:", data["meeting"])
