# -*- coding: utf-8 -*-
from lxml import html
import requests


linki = 'individual page to scrape'
page = requests.get(linki)
tree = html.fromstring(page.content)
name = tree.xpath('//span[@class="fn org"]')[0].text
street = tree.xpath('//strong[@class="street-address"]')[0].text
post = tree.xpath('//span[@class="postal-code"]')[0].text
city = tree.xpath('//span[@class="locality"]')[0].text
web = tree.xpath('//a[@class="url"]')[0].text
tel = tree.xpath('//span[@class="tel"]/text()')

name = name.encode('ascii', 'ignore')
street = street.encode('ascii', 'ignore')
post = post.encode('ascii', 'ignore')
city = city.encode('ascii', 'ignore')
#tel = tel.encode('ascii', 'ignore')
web = web.encode('ascii', 'ignore')
print str(name) + "|" + str(street) + "|" + str(post) + "|" + str(web) + "|"+ str(tel) + "\n"
with open("file to write  result", "a") as files:
    files.write(str(name) + "|" + str(street) + "|" + str(post) + "|" + str(web) + "|"+ str(tel) + "\n")
files.close()