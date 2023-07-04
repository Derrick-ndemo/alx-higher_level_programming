#!/bin/bash
# script that takes URL sends a post request and displays body
curl -s -X POST -d "test@gmail.com&subject=I will always be here for PLD" "$1"
