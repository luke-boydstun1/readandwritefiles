import csv

in_file = open("sales.csv", "r")
out_file = open("salesreport.csv", "w")

data = csv.reader(in_file, delimiter=',')

count = 0
transactions = []

for row in data:
    if count != 0:
        id = row[0]
        total = float(row[3])+float(row[4])+float(row[5])
        transaction = [int(id), total]
        transactions.append(transaction)
    count += 1

entries = len(transactions)

id_total = 0
id = 250

for i in transactions:

    if i[0] == id:
        id_total += float(i[1])

    else:
        line = str(id) + ' ' + str(id_total) + '\n'
        out_file.write(line)
        id_total = float(i[1])
        id += 1


out_file.close()
