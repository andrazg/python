import urllib
import lxml.html
from lxml import html
import requests


connection = urllib.urlopen('web page')
dom = lxml.html.fromstring(connection.read())
for link in dom.xpath('//a/@href'):
    page = requests.get(link)
    tree = html.fromstring(page.content)
    name = tree.xpath('//span[@class="fn org"]')[0].text()
    print name