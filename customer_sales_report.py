import csv

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

sales = csv.reader(infile, delimiter=",")
next(sales)

outfile.write("Customer ID" + ", " + "Calculated Total" + "\n")
# outfile.write("____________________________________________________" + "\n")

cust_total = 0
customer_id = ""

for x in sales:
    if x[0] != customer_id:
        if customer_id:
            outfile.write(customer_id + ", " + format(cust_total, ".2f") + "\n")
        cust_total = 0
        customer_id = x[0]

    subtotal = float(x[3])
    taxamt = float(x[4])
    freight = float(x[5])
    total = subtotal + taxamt + freight
    cust_total += total
outfile.write(customer_id + ", " + str(format(cust_total, ".2f")) + "\n")
