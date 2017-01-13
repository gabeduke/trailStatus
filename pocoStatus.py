#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

link = "http://www.canarypartners.com/fopsp/widget.php?city=Richmond&park=poca&state=VA&bg=F8F8F8&fr=1&amt=1&delay=1%27;%20var%20suffix%20=%20%27&output=xml"
response = urllib2.urlopen(link)
page_source = response.read()
soup = BeautifulSoup(page_source, 'html.parser')
alert = soup.find(id="alert")

print(alert.get_text())
