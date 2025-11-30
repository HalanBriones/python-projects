import pandas as pd
from sqlalchemy import create_engine


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql, dbconnection):
    print("\n*** Showing SQL statement")
    print(sql)
    # Perform query
    subDf = pd.read_sql(sql, dbconnection)
    print("\n*** Showing dataframe summary")
    return subDf

# PATH = '../lab10/'
# CSV_DATA = 'brazil_forestFires.csv'
# df = pd.read_csv(PATH+CSV_DATA,skiprows=1,encoding = "ISO-8859-1" ,sep=',',names=('year','state','month','number','date'))
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 1000)
# print(df)
#create database
DB_FILE    = 'ramenReviews.db'
PATH = '../../'

engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()
# df.to_sql(name='table_name', con=connection, if_exists='replace', index=False)

# Get DataFrame contents for 'Rio' and 'Sao Paulo' only.
sql = "SELECT * FROM " + "Review"

newDf = showQueryResult(sql, connection)
print(newDf)