import csv 

data=[]
with open("PRO-129-Datasets-main/archive_dataset.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data.append(i)
headers=data[0]
planet_data=data[1:]
for data in planet_data:
    data[2]=data[2].lower()
print(planet_data[0])
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("sorted.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
with open("sorted.csv") as input, open("sorted1.csv","w",newline="") as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)