#!/bin/bash

API_KEY_SECRET="bytepixelsfu_default_secret"
bytepixel_URL="https://sfu.bytepixel.com/api/v1/meetings"
#bytepixel_URL="http://localhost:3010/api/v1/meetings"

curl $bytepixel_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --request GET
