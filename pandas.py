import csv


with open("data.csv") as d:
    man = 0
    woman = 0
    podatki = csv.reader(d,delimiter=";")
    counter = sum(1 for i in podatki)-1
    for i in podatki:
        if i[1] == 'm':
            man +=1
        if i[1] == 'f':
            woman +=1
    print "Men have watched: " + str(man) + " movies and" + " Women have watched a total of: " +str(woman) +" movies " + \
          "In percentage:"

