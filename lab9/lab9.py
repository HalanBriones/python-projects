import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "../../retailer_data.txt"
df       = pd.read_csv(PATH,skiprows=1,sep=',', names=('productID','productName','vendor','quantity','price','stockDate'))

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine     = create_engine('sqlite://', echo=False) #here you change if you have a real DataBase
    connection = engine.connect()
    df.to_sql(name='RetailInventory', con=connection, if_exists='replace', index=False)#this allow to act as a db because
    #we dont have one in this case

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# Read all rows from the table.
# SQL     = "SELECT * FROM RetailInventory"
SQL     = "SELECT vendor, price*quantity AS revenueValue FROM RetailInventory GROUP BY vendor HAVING vendor='Silverware Inc.' OR vendor='Waterford Corp.'"
results = showQueryResult(SQL)
print(results)
