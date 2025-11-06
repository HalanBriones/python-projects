#Data frames transform a dictionary into a table with columns and rows
import pandas as pd
#refering a doc txt csv with information to work on
path = "random_body_data.txt"
df = pd.read_csv(path,skiprows=1,sep='\t',names=('Density', 'Pct.BF', 'Age',   'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen',  'Waist', 'Hip',  'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))
#rename the columns names axis=0\rows(index) axis=1\columns
df=df.rename({'Pct.BF':'Pct BF'},axis=1)
print(df)
#creation of a dictionary
dict_add={'Density':[1.0101,1.0202], 'Pct BF':[10.1,10.5],'Age':[34,43],'Weight':[82.1,89.4],'Height':[182.1,178.4],
                           'Neck':[32.0,30.1],'Chest':[95.9,90.4],'Abdomen':[88.4,100.4],'Waist':[92.0,102.3], 'Hip':[92.4,94.1],'Thigh':[60.1,62.3],
                          'Ankle':[20.5,22.4],'Knee':[42.1,43.8],'Bicep':[27.2,30.1],'Forearm':[21.1,20.3],'Wrist':[16.2,15.1]}
#transform a dictionary to a dataframe
df_dict = pd.DataFrame(dict_add,columns=['Density','Pct BF','Age','Weight','Height',
                                'Neck','Chest','Abdomen','Waist', 'Hip','Thigh',
                                'Ankle','Knee','Bicep','Forearm','Wrist'])
# print("Dictionary to dataframe Add-on \n",df_dict)
#concat two data dataframes together
df = pd.concat([df,df_dict]).reset_index(drop=True)
# print(df)
#count total of rows but DO NOT count NaN or None
print("Count() \n",df.count())
#show a quick understanding of the columns ranges and frequency of each value
print("Value_Counts() \n",df.value_counts())
# get the uniques values from a column
#.unique()
# Show all columns.
pd.set_option('display.max_columns', None)
# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

#Excercise 1
df2 = df[['Height','Waist','Weight','Pct BF']] #Creating a dataframe base in columns of other dataframe
df2 = df2.rename({'Pct BF':'Percent Body Fat'},axis=1)
print(df2)
