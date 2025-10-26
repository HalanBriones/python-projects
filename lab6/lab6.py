'''
numbers = [1.3,2.6,8.9,11.5,14.8]

for i  in range(len(numbers)):
   print(f"index {str(i)}- {str(numbers[i])}")

for numbers in numbers:
    print(numbers)
'''
#sorted list
# def showFruitList(fruitList):
#     print("\n*** DISPLAYING ARRAY CONTENTS")
#
#     # Loop from 0 to 1 - length of array.
#     for i in range(len(fruitList)):
#         print(fruitList[i])
# # Create array.
#
# fruit = ["apples"]

# Add items to array.
# fruit.append("bananas")
# fruit.append("pears")
# fruit.insert(0, "plums")
# Show array contents.
# showFruitList(fruit)
# Remove third element (counting starts at 0).
# fruit.pop(2)

# Show array contents.
# showFruitList(fruit)
# fruit.sort()
# print(fruit)

# dataSet = {'First Name': ['Jonny','Holly','Nira'],'Last Name':['Stuab','Aurora','Conway'],
#            'Grade': [85,95,91]}
#
# # Create dataframe with data set and named columns.
# # Column names must match the dataSet properties.
# df = pd.DataFrame(dataSet, columns= ['First Name','Last Name', 'Grade'])
#
# # Show DataFrame
# print(df)
# Create data set.
# dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
#            'Last': [2932.05, 26485.01, 21087.16] }

# Create dataframe with data set and named columns.
# df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
#
# # Show original DataFrame.
# print("\n*** Original DataFrame ***")
# print(df)
#
# # Create change column.
# change = [-21.51, -98.41, -453.83]
# percentage_change=['S&P 500 -0.73', 'Dow -0.37', 'Nikkei -2.11']
# # Append change column.
# df['Change'] = change
# df['Percentage Change']= percentage_change
#
# # Show revised DataFrame.
# print("\n*** Adjusted DataFrame ***")
# print (df)

# dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
#            'Last': [2932.05, 26485.01, 21087.16] }
#
# # Create dataframe with data set and named columns.
# df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
#
# # Show original DataFrame.
# print("\n*** Original DataFrame ***")
# print(df)
#
# # Add new line.
# print("\n")
#
# # Show names only
# for i in range(len(df)):
#     print(df.loc[i]['Last'])
#
# print("Printing the first row")
# print(df.loc[0])
# import pandas as pd
# # Create data set.
# dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
#            'Last': [2932.05, 26485.01, 21087.16] }
#
# # Create dataframe with data set and named columns.
# df1 = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
#
# # Show original DataFrame.
# print("\n*** Original DataFrame ***")
# print(df1)
# dataSet2 = { 'Market': ['Hang Seng', 'DAX'],
#              'Last': [26918.58, 11872.44]}
# df2 = pd.DataFrame(dataSet2, columns= ['Market', 'Last'])
# print("\n*** Original DataFrame 2 ***")
# print(df2)
# df1 = df1._append(df2)
# print("\n*** Adjusted DataFrame ***")
# print(df1)
#
# dataSet3 = {'Market':['FTSE100'],'Last':[7407.06]}
# df3 = pd.DataFrame(dataSet3,columns=['Market','Last'])
# df1 = df1._append(df3)
#
# print("\n*** Adjusted DataFrame ***")
# print(df1)

# import pandas as pd
#
# # Create data set.
# dataSet = {'Market': ['S&P 500', 'Dow', ],
#            'Last': [2932.05, 26485.01 ]}
#
# # The dictionary is an object made of name value pairs.
# stockDictionary = {'Market': 'Nikkei', 'Last': 21087.16 }
#
# # Create dataframe with data set and named columns.
# df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
#
# # Show original DataFrame.
# print("\n*** Original DataFrame ***")
#
# df = df._append(stockDictionary, ignore_index=True)
# print(df)
#
# dict = {'Market':['DAX'],'Last':[11872.44]}
# dict_df = pd.DataFrame(dict,columns =['Market','Last'])
# print("Adjusted DataFrame")
# df = pd.concat([df,dict_df]).reset_index(drop=True)
# print(df)
#
# pd.set_option('display.max_columns', None)
#
# # Increase number of columns that display on one line.
# pd.set_option('display.width', 1000)
#
# print("\n FIRST 2 ROWS") # Prints title with space before.
# print(df.head(2))
#
# print("\n LAST 2 ROWS")
# print(df.tail(2))
#
# # Show data types for each columns.
# print("\n DATA TYPES") # Prints title with space before.
# print(df.dtypes)
#
# # Show statistical summaries for numeric columns.
# print("\nSTATISTIC SUMMARIES for NUMERIC COLUMNS")
# print(df.describe())
#
# # Show summaries for objects like dates and strings.
# print("\nSTATISTIC SUMMARIES for DATE and STRING COLUMNS")
# print(df.describe(include=['object']))

import pandas as pd
path = "../random_body_data.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age',   'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen',  'Waist', 'Hip',  'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

print("First 2 Rows \n " , df.head(2))

print("Last 2 Rows \n", df.tail(2))

print("Data Types \n",df.dtypes)

print("Stadistics \n ", df.describe().round(2))

df2 = df[["Height", "Waist", "Weight","Pct.BF"]]

print("Subset \n", df2)