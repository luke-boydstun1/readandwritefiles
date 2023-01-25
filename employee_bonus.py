import csv

in_file = open("EmployeePay.csv", "r")

data = csv.reader(in_file, delimiter=',')

for row in data:
    line = ''
    for i in row:
        line += i + ' '
    print(line)
