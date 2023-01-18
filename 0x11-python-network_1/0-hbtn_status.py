#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

site = 'https://alx-intranet.hbtn.io/status'
if __name__ == "__main__":
    with urllib.request.urlopen(site) as response:  # opens the site
        html = response.read()  # read what is on the site
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
