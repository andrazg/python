from lxml import html
import requests

with open("file with links to rank", "r") as fi:
    for i in fi:
        page = requests.get('http://www.alexa.com/siteinfo/' + i)
        tree = html.fromstring(page.content)
        rank = tree.xpath('//strong[@class="metrics-data align-vmiddle"]/text()')
        print unicode(rank),"|",i
