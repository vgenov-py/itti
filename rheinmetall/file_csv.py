import csv
import gzip

"SIN MÓDULO CSV: "
with open("result.csv", "r", encoding="utf-8") as file:
    data = file.readlines()
    data = [r.split(";") for r in data]
    headers = data[0]
    for row in data[1:]:
        if row[0].startswith("RHM"):
            # print(row[2])
            pass

"CON MÓDULO CSV: "
with open("result.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file, delimiter=";")
    data = list(csv_reader)
    # FILE CLOSED

# data.append(["LMT;1", 400, 300.33])
for row in range(100000): # O(n)
    data.append("XXX;XXX;XXX")

with open("result.csv", "w") as file:
    csv_writer = csv.writer(file, delimiter=";")
    # csv_writer.writerows(data) # O(n)
    for row in data: 
        csv_writer.writerow(row) # O(n)

"CSV compress:"

with gzip.open("result.csv.gz", "wt") as file:
    csv_writer = csv.writer(file, delimiter=";")
    # csv_writer.writerows(data) # O(n)
    for row in data: 
        csv_writer.writerow(row) # O(n)