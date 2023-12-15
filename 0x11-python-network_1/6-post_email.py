#!/usr/bin/python3
"""A script that:
- first takes a URL,
- then sends a request to that URL and shows the value
- of the X-Request-Id variable found in the response header.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
