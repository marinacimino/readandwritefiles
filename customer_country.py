import csv

infile = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")

customers = csv.reader(infile, delimiter=",")
next(customers)

outfile.write("Last Name" + ", " + "First Name" + ", " + "Country" + "\n")
# outfile.write("____________________________________________________" + "\n")

for x in customers:
    last_name = x[1]
    first_name = x[2]
    country = x[4]
    outfile.write(last_name + ", " + first_name + ", " + country + "\n")
