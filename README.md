# LCC Spending Data 

## What is it?

Liverpool City Council report  on, and provide details for, invoices over £500 made for the supply of goods and services. 

In [the council's own words](http://liverpool.gov.uk/council/performance-and-spending/budgets-and-finance/transparency-in-local-government/):

	This is so that you know where your money is being spent, and for better scrutiny of spending.


This tool attempts to aggregate and show the data in a more useful format for those that don't like wrangling XLS/CSV files.


## Setup 

```bash
   virtualenv .
   . bin/activate 
   git clone https://github.com/Liverpool-UK/lcc-spending.git
   cd lcc-spending
   python setup.py develop
   
   # May need to be run as postgres user 
   createdb lcc_spending -E utf8 
   psql lcc_spending -f migrations/*.sql
   
   import_over500 
```