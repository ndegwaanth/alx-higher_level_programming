#!/bin/bash
# send the Get request to the url and
# display the body of the response

# Check if the user provided a URL
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Send a GET request to the URL using curl and display the body of the response
response=$(curl -s -w "%{http_code}" -o response.txt "$url")

# Extract the status code from the response
status_code=$(tail -n1 response.txt)

# Check if the status code is 200
if [ "$status_code" -eq 200 ]
then
    cat response.txt  # Display the body of the response
fi

# Clean up the response file
rm -f response.txt
