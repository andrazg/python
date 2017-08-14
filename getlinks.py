import urllib
import lxml.html
from lxml import html
import requests

WEB = "google.si"
xpatWebpage = "span[]something.txt()"



connection = urllib.urlopen(web)
dom = lxml.html.fromstring(connection.read())
for link in dom.xpath('//a/@href'):
    page = requests.get(link)
    tree = html.fromstring(page.content)
    name = tree.xpath(xpatWebpage)
    print name