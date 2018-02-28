#!/usr/bin/env python3

"""Train delay from my home to the main station

This file parses the website of Deutsch Bahn to check if any trains are late
and prints out the next trains from my home to the main station including
their delay
"""

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def has_the_right_class(tag):
    """Selector for the field of the train delay"""
    return tag.has_attr('class') and "time" in tag['class'] \
        and tag.parent.has_attr('class') and "firstrow" in tag.parent["class"]


def main():
    """Main method. query website and prints times """
    url = 'https://reiseauskunft.bahn.de/bin/query.exe/dn'
    post_fields = {
        """The starting train station"""
        'REQ0JourneyStopsS0ID': u'A=1@O=Empelde@X=9668986@Y=52340160' +
        '@U=81@L=008001781@B=1@p=1516311829@',
        """The destination train station"""
        'REQ0JourneyStopsZ0ID': u'A=1@O=Hannover Hbf@X=9741017@Y=52376764@' +
        'U=80@L=008000152@B=1@p=1511926111@',
        """Has to be given as an extra attribute"""
        'start': 'Suchen'
    }
    request = Request(url, urlencode(post_fields).encode())
    html_doc = urlopen(request).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    for link in soup.find_all(has_the_right_class):
        print("time " + link.get_text().strip())


if __name__ == "__main__":
    main()
