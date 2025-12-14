import pandas as pd
from   sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "C:\\datasets\\"

 # Create the database at the specified path.
DB_FILE    = 'forestFire.db'
engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql, dbconnection):
    print("\n*** Showing SQL statement")
    print(sql)
    # Perform query
    subDf = pd.read_sql(sql, dbconnection)
    print("\n*** Showing dataframe summary")
    return subDf

# Get DataFrame contents for 'Rio' and 'Sao Paulo' only.
sql = "SELECT * FROM " + "brazilForest" \
      + " WHERE state = 'Rio' OR state='Sao Paulo' " \
      + " ORDER BY date"

newDf = showQueryResult(sql, connection)
print(newDf.tail())
