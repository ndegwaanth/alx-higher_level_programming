#!/usr/bin/python3
""" This script sends a POST request to http://0.0.0.0:5000/search_user
    with a letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
