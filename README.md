# LCC Spending Data 



## Setup 

```bash
   virtualenv .
   . bin/activate 
   git clone https://github.com/Liverpool-UK/lcc-spending.git
   cd lcc-spending
   pip install -r requirements.txt 
   
   # May need to be run as postgres user 
   psql createdb lcc_spending -E utf8 
```