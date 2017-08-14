from lxml import html
import requests

page = requests.get('individual page to scrape')
tree = html.fromstring(page.content)
name = tree.xpath('//div[@class="ofctitle"]/text()')
phone = tree.xpath('//div[@class="ofcphone"]/text()')
email = tree.xpath('//a[@href="mailto:"]/text()')
#address = tree.xpath('//d[@class="metrics-data align-vmiddle"]/text()')

print name, phone, email