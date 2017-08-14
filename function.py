import csv

with open("data.csv") as d:
    man = 0
    women = 0
    podatki = csv.reader(d,delimiter=";")

    for i in podatki:
        if i[1] == 'm':
            man +=1
        if i[1] == 'f':
            women +=1
    print "Men have watched: " + str(man) + " movies and" + " Women have watched : " +str(women) +" movies"
