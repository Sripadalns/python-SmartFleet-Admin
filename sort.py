import csv
import operator

datafile =open('output-2015.csv',"rb")
reader=csv.reader(datafile)
sort = sorted(reader,key=operator.itemgetter(5))
for eachline in sort:
    print eachline
output=open('output.csv',"wb")
writer = csv.writer(output)
 
for eachline in sort:
    writer.writerow(eachline)
 
datafile.close()
output.close()
