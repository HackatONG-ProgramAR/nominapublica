#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Scrapper para los documentos con las nominas de la municipalidad de Jesus Maria.
"""

import json
import sys
import requests
from urlparse import urljoin
from pdftables.pdftables import PDFDocument


INFILE = "../nominas/jesusmariares.json"
OUTFILE = "../nominas/filename.csv"

class JMScrapper(object):
    """
    """
    def __init__(self, infile=INFILE):
        self._infile = infile
        self._results = []

    def download(self, url):
        outfile = url
        with open(outfile, 'wb') as handle:
            response = requests.get(url, stream=True)
            if not response.ok:
                print 'error'

            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)

def main():
    """
    """

    filepath = "../nominas/perman.julio_.14.pdf"
    #with open(filepath, 'w') as fileobj:
    fileojb = open(filepath, 'rb')
    


if __name__ == "__main__":
    main()
    sys.exit()

