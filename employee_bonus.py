import csv

in_file = open("EmployeePay.csv", "r")

data = csv.reader(in_file, delimiter=',')

count = 0
for row in data:
    if count != 0:
        amount = float(row[3]) * (1+float(row[4]))

        line = row[1] + ' ' + row[2] + ": " + str(amount)
        print(line)
    count += 1
