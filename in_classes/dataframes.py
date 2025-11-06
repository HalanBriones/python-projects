#Dictionary structure key-value

students= {'Alice': 24, 'Bob':27,'Dan':21, 'Emma':23}
print(students) #.keys()-.values()

keys_students= list(students.keys()) #save keys in a list
print(keys_students[2])

#Data Frame organize data into a table of rows and columns(Excel sheet)
import pandas as pd
#Use simple coutes
dataSet = {"First Name":['Jony','Holly','Nira'],"Grade":[85,95,91]}
df = pd.DataFrame(dataSet, columns=["First Name","Grade"])
print(df)
#add Column
# df["Class"]=["Math","History","Biology"] #make sure you pass the same amount of to the amount of values
df['Class']="Math" #I f you pass one value will fill up the other with the same content
print(df)
#Modify the first value
df.loc[0,"Grade"]=50 #you can use loop to change information

print(df)
#Change column Names
# new_df = df.rename({'First Name':'FirstName','Grade':'Grades'},axis=1) #axis=1 = value axis=0
# print("new df \n",new_df)

print(df.loc[0]["First Name"]) #first first values
#Use notepad to open csv, txt docs not excel, excel can give you some troubles

#Value_counts you get a quick understanding of the column ranges and frequency for each value

#Count: total of numbers of rows (Do Not count NaN or None value)
#get uniques values froma colum
# df['A'].unique()

#Sort values Data Frame in final exam

#filtering dataframe
#numeric dataframe summaries
#group by


#Key arguments or position arguments but dont mix them speaking about functions

unformattedFloat = 233.654
wholeNumber = str(unformattedFloat)
print(type(wholeNumber))
print(wholeNumber)

newFormattedInt = int(unformattedFloat)
print(type(newFormattedInt))
print(newFormattedInt)
print(type(unformattedFloat))
