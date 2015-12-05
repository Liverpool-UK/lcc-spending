# coding=UTF-8
from dateutil import parser
import os
import re

import unicodecsv as csv

from spending.database.models import Over500
from spending.database.connection import get_connection

TOCLEAN = {
    "Adult Services & Hea": u"Adult Services & Health",
    "Regeneration & Emplo": u"Regeneration & Employment",
    "Children & Young Peo": u"Children & Young People",
    "Capital Leisure Serv": u"Capital Leisure Services",
    "Capital Regen": u"Capital Regeneration",
    "Car Parks Mgt Genera": u"Car Parks Mgt General",
}

def cleaner(cell):
    return TOCLEAN.get(cell, cell)

def upsert_data(data):
    pass

def log_line(s):
    print u"{0}\r".format(s),

def main():
    print "Importing data for over £500 spend data"

    db = get_connection()

    ids = []

    # We HAVE to delete all entries where sap_document == "" and force a re-import
    # because they are from malformed
    # db.query(Over500).filter(Over500.sap_document == "").delete()

    count = 0
    spending_data = os.path.join(os.getcwd(), "data/spending.csv")
    with open(spending_data, "r") as f:
        reader = csv.reader(f)
        reader.next()

        for row in reader:
            service_area = cleaner(row[0])
            expense_type = cleaner(row[1])
            sap_document = row[2]
            posting_date = parser.parse(row[3])
            vendor = row[4]
            amount = row[5]
            month = posting_date.month
            year = posting_date.year

            # If sap_document looks like 005.2015 then there is no sap_document ...
            # for these we will make a hash of the
            if re.match('[0-90-90-9]\.[0-90-90-90-9]', sap_document.strip()):
                sap_document = ""

            e = Over500()
            e.sap_document = sap_document
            e.service_area = service_area
            e.posting_date = posting_date
            e.vendor = vendor
            e.expense_type = expense_type
            e.amount = float(amount)
            e.year = year
            e.month = month

            db.add(e)

            count = count + 1
            log_line("Process item {0}".format(count))

    db.commit()
    db.close()





