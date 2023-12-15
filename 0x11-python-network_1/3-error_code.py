#!/usr/bin/python3
"""A script that:
- first takes a URL,
- then sends a request to that URL
- and displays the response body(decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
