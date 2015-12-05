# coding=UTF-8
from dateutil import parser
import os
import csv


TOCLEAN = {}

def cleaner(cell):
    return TOCLEAN.get(cell, cell)

def main():
    print "Importing data for over £500 spend data"

    spending_data = os.path.join(os.getcwd(), "data/spending.csv")
    with open(spending_data, "r") as f:
        reader = csv.reader(f)
        reader.next()

        for row in reader:
            date = parser.parse(row[3])
            d = dict(
                service_area = cleaner(row[0]),
                expense_type = cleaner(row[1]),
                sap_document = row[2],
                posting_date = date,
                vendor=row[4],
                amount = row[5],
                month = date.month,
                year = date.year)
            print d







