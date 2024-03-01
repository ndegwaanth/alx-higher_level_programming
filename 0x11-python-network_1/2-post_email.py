#!/usr/bin/python3
""" This script sends a POST request to a URL with an email as a 
    parameter and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    try:
        # Send a POST request with the email parameter
        with urllib.request.urlopen(url, data=data) as response:
            # Read and decode the response body
            body_response = response.read().decode('utf-8')
            print(f"Your email is: {body_response}")
    except urllib.error.URLError as e:
        print("Error accessing URL", e)
