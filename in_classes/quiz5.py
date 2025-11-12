import pandas as pd

PATH = "age_cholesterol_data.txt"


df = pd.read_csv(PATH, skiprows=1,sep=',',names=('age','Mean Cholesterol Level','Total People'))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
age_list=list(df['age'])
cholesterol_list=list(df['Mean Cholesterol Level'])

for i in range(len(age_list)):
    print(f'Age: {age_list[i]}')
    for x in range(len(cholesterol_list)):
        if i==x:
            print(f'Mean Cholesterol Level: {cholesterol_list[x]}')
            break