#!/bin/bash

API_KEY_SECRET="bytepixelsfu_default_secret"
bytepixel_URL="https://sfu.bytepixel.com/api/v1/join"
# bytepixel_URL="http://localhost:3010/api/v1/join"

curl $bytepixel_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --data '{"room":"test","roomPassword":"false","name":"bytepixelsfu","audio":"true","video":"true","screen":"false","hide":"false","notify":"true","token":{"username":"username","password":"password","presenter":"true", "expire":"1h"}}' \
    --request POST