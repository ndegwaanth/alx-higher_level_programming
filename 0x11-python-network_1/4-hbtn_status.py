#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status
    using the requests library.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content: ", response.text)