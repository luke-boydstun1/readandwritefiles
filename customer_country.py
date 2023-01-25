import csv

in_file = open("customers.csv", "r")
out_file = open("customer_country.csv", "w")

data = csv.reader(in_file, delimiter=',')

for row in data:
    name_country = row[1] + ',' + row[4] + '\n'
    out_file.write(name_country)

out_file.close()
