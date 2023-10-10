import csv

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

data.append(["LMT;1", 400, 300.33])
for row in data:
    print(row)
with open("result.csv", "w", encoding="utf-8") as file:
    csv_writer = csv.writer(file, delimiter=";")
    csv_writer.writerows(data)