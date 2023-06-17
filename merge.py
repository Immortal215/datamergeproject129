import csv 

data1=[]
data2=[]
with open("PRO-129-Datasets-main/final.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data1.append(i)
header1=data1[0]
planet_data1=data1[1:]
with open("PRO-129-Datasets-main/sorted1.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data2.append(i)
header2=data2[0]
planet_data2=data2[1:]
headers=header1+header2
planet_data=[]
for index,data in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open("merge.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
with open("PRO-129-Datasets-main/merge.csv") as input, open("merge1.csv","w",newline="") as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)