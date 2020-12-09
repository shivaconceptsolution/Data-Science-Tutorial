import csv
with open('data.csv','rt')as f:
  #data = csv.reader(f)
  data = csv.DictReader(open("data.csv"))  
  for row in data:
        print(row)
