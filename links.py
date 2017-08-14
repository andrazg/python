import urllib
import lxml.html

with open("file with links", "r") as files:
    for i in files:
        stran = urllib.urlopen(i)
        branjestrani = lxml.html.fromstring(stran.read())
        for link in branjestrani.xpath('//a/@href'):
            with open("file to append links", "a") as myfile:
                myfile.write(str(link+ '\n'))
                myfile.close()
files.close()

