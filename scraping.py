# -*- coding: utf-8 -*-
from lxml import html
import requests



with open("file with links", "r") as files:
    for link in files:
        page = requests.get(link)
        tree = html.fromstring(page.content)
        name = tree.xpath('//span[@class="fn org"]')[0].text
        street = tree.xpath('//strong[@class="street-address"]')[0].text
        post = tree.xpath('//span[@class="postal-code"]')[0].text
        city = tree.xpath('//span[@class="locality"]')[0].text
        tel = tree.xpath('//span[@class="tel"]/text()')
        web = tree.xpath('//a[@class="url"]')[0].text
        while True:
            try:
                print name, ",", street, ",", post, ",", city,",", web,",",tel
                break
            except:
                pass


        #with open("d:/spain/end.txt", "a") as result:
         #   result.write(name)
        #result.close()
files.close()

