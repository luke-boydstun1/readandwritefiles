import csv

in_file = open("sales.csv", "r")
out_file = open("salesreport.csv", "w")

data = csv.reader(in_file, delimiter=',')

count = 0

for row in data:
    if count != 0:
        total = float(row[3])+float(row[4])+float(row[5])
        line = row[0] + ' ' + str(total) + '\n'
        out_file.write(line)
    count += 1

out_file.close()
