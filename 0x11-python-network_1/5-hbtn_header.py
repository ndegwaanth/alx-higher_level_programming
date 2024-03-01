#!/usr/bin/python3
""" This script takes a URL, sends a request, and displays
    the value of the X-Request-Id header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(f"{x_request_id}")
    else:
        print("X-Request-Id header not found in the response.")
