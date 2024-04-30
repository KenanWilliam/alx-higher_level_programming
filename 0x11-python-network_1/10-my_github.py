#!/usr/bin/python3
"""
takes your Github credentials
(username and password)
and uses the Github API to display your id
"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    u = argv[1]
    p = argv[2]
    rps = requests.get(
        "https://api.github.com/user",
        auth=(HTTPBasicAuth(u, p)))
    try:
        r = rps.json()
        print(r.get('id'))
    except Exception:
        print('None')
