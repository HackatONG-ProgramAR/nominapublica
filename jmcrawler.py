#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crawler para bajar los documentos con las nominas de la municipalidad de Jesus Maria.
"""

import json
import sys
import requests
from urlparse import urljoin
from bs4 import BeautifulSoup


OUTFILE = "jesusmariares.json"
ENTRY_COUNT = 10

class JMCrawler(object):
    """
    """
    def __init__(self, amount=ENTRY_COUNT):
        self._url = "http://www.jesusmaria.gov.ar/transparencia/planta-permanente/" 
        self._content = ""
        self._results = []

    def get_html(self):
        req = requests.get(self._url)
        data = req.text#.decode('utf-8')
        #self._content = data
        return data

    def parse(self, content):
        soup = BeautifulSoup(content)
        entries = soup.find_all('div', {"class" : "one-fourth"})
        for entry in entries:
            links = entry.find_all('a', href=True)
            for link in links:
                result = {}
                doc = link.get_text()
                if doc == "Descargar PDF":
                    result['link'] = link.get("href")
                self._results.append(result)

        return self._results

    def print_results(self):
        print ""
        for result in self._results:
            print "{0}".format(result['link'])

def main():
    """
    """
    crawler = JMCrawler()
    content = crawler.get_html()
    results = crawler.parse(content)
    crawler.print_results()
    with open(OUTFILE, 'w') as outfile:
        json.dump(results, outfile)

if __name__ == "__main__":
    main()
    sys.exit()

