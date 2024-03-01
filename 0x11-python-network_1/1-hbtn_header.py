#!/usr/bin/python3
""" This script sends a request to a URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error accessing URL:", e)
