#!/bin/bash
# Send a JSON post req to a given url
curl -s -H "Content-Tyle: application/json" -d "$(cat "$2")" "$1"
