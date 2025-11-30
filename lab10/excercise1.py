import pandas as pd
DRIVER_PATH        = "../../extras/"
CSV_FILE    = 'retailerDB.txt'
df      = pd.read_csv(DRIVER_PATH+CSV_FILE, skiprows=1, sep=',',names=('productID','productName','vendor','quantity','price''stockDate'))

# Here I have decided to use a tab separator.
# The default separator is a comma which also could work.
# dfOut.to_csv(DRIVER_PATH + CSV_FILE, sep=',') #transform a dataframe in to a doc csv

# Since I saved the file with a tab separator the instruction
# that reads the content must also use a tab separator.
# dfIn = pd.read_csv(DRIVER_PATH + CSV_FILE,index_col=0)#read the doc txt
print(df)
