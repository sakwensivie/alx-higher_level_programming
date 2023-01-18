#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request and the value of the X-Request-Id
variable found in the header."""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopne(sys.argv[1]) as response:
        html - response.info()
        print(html.get('X-Request-Id'))
