#!/usr/bin/bash

# Check if the user provided a URL
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Send a request to the URL using curl and get the size of the response body in bytes
size=$(curl -s "$url" | wc -c)

# Display the size of the body of the response
echo "$size"
