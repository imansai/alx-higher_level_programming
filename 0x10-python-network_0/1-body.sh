#!/bin/bash
# Checks if  URL is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Ges URL from CL argument
url="$1"
response_headers=$(curl -sI "$url")
http_status=$(echo "$response_headers" | grep -i "^HTTP" | awk '{print $2}')
if [ "$http_status" -eq 200 ]; then
    curl -sL "$url"
else
    echo "HTTP Status Code: $http_status"
    echo "Failed to retrieve the URL: $url"
    exit 1
fi
