from csv import DictReader

file1=open("home_drilled.csv","r",encoding="utf8")
file2=open("High_drilled.csv","r",encoding="utf8")
csv1=DictReader(file1)
csv2=DictReader(file2)
for row in csv1:
    print(row)

for row in csv2:
    print(row)

file1.close()
file2.close()