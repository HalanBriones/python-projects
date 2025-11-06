import pandas as pd

# Import data into a DataFrame.
path = "babysamp_98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
# Rename the columns so they are more reader-friendly.
df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method
# Show all columns.
pd.set_option('display.max_columns', None)
# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
# print("\nTOP FREQUENCY FIRST")
# print(df['Mom Age'].value_counts())
#
# print("\nLOWEST FREQUENCY FIRST")
# print(df['Mom Age'].value_counts(ascending=True))
#
# print("\nFREQUENCY SORTED by MOTHER AGE")
# print(df['Mom Age'].value_counts().sort_index())

#Excercise 2
# print(df['Mom Edu'].value_counts().sort_index())
# Sort by descending mother age and then by ascending weight.
dfSorted = df.sort_values(['Mom Age', 'Weight'], ascending=[False, True])
# print(dfSorted)
#Excercise 3
dfSorted2 = df.sort_values(['gestation','Weight'],ascending=[True,True])
# print(dfSorted2)
'''
Numeric DataFrame Summary functions 
count()	Number of non-null observations
sum()	Sum of values
mean()	Mean of values (average)
median	()	Arithmetic median of values (the value is in the middle in an order column)
min()		Minimum
max()		Maximum
std()	Unbiased standard deviation (variability or variation)
'''
#Excercise 4
# Compound conditions require single '&' for 'AND' and single '|' for 'OR.
resultDf = df[(df['Dad Age']>=40) & (df['Mom Age'] >= 40)]
# print(resultDf)
# print(f'Count:{df['Mom Age'].count()}\nMin:{df['Mom Age'].min()}\nMax:{df['Mom Age'].mean()}\nMedian:{df['Mom Age'].median()}\nStandarDeviation:{df['Mom Age'].std()}')
#Exercise 5 and 6 in the word document
#Exercise 7 Using the baby sample, group on either male or female and show the maximum weight, minimum weight,
# and mean weight. Show your program here. (No screenshots please):
df2 = df.groupby('sex')['Weight'].max().reset_index().rename(columns={'Weight':'Max Weight'})
dfMinWeight = df.groupby('sex')['Weight'].min().reset_index().rename(columns={'Weight':'Min Weight'})
dfMeanWeight = df.groupby('sex')['Weight'].mean().reset_index().rename(columns={'Weight':'Mean Weight'})
df2['Min Weight'] = dfMinWeight['Min Weight']
df2['Mean Weight'] = dfMeanWeight['Mean Weight']
final_df2 = df2[(df2['sex']=='M')]
print(final_df2)
#Rest of excercise are in the word
