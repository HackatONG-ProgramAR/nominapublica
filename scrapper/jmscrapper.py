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

class JMScrapper(object):
    """
    """
    def __init__(self):
        self._content = ""
        self._results = []


def main():
    """
    """
    filepath = "../nominas/perman.octubre.11.web_.pdf"
    #with open(filepath, 'w') as fileobj:
    fileojb = open(filepath, 'rb')
    


if __name__ == "__main__":
    main()
    sys.exit()

