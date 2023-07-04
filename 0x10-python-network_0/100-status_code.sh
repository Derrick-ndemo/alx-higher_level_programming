#!/bin/bash
# Send a Get req to a given URL and display the respoonse status code
curl -s -o /dev/null -w "%{http_code}" "$1"
