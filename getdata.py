from lxml import html
import requests
with open("d:/spain/total_lin.txt") as lini:
    for i in lini:
        page = requests.get(i)
        tree = html.fromstring(page.content)
        name = tree.xpath('//span[@class="fn org"]/text()')
        street = tree.xpath('//strong[@class="street-address"]/text()')
        post = tree.xpath('//span[@class="postal-code"]/text()')
        city = tree.xpath('//span[@class="locality"]/text()')
        tel = tree.xpath('//span[@class="tel"]/text()')
        web = tree.xpath('//a[@class="url"]/text()')
        votes = tree.xpath('//div[@class="left title 1"]/text()')
        with open("d:/spain/end.txt", "a") as filess:
            filess. write(str(name)+","+ str(street)+","+str(post)+","+str(city)+","+str(tel)+","+str(web)+","+str(votes)+"\n")
        filess.close()
lini.close()

