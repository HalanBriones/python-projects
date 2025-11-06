# import numpy as np
# import matplotlib.pyplot as plt

# years       = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
# colorado    = [5029196,5029316,5048281,5121771,5193721,5270482,5351218,5452107,
#                5540921,5615902,5695564]
# connecticut = [3574097,3574147,3579125,3588023,3594395,3594915,3594783,3587509,
#                3578674,3573880,3572665]
# delaware    = [897934,897934,899595,907316,915188,923638,932596,941413,949216,
#                957078,967171]
#
#
# # red dashes, blue squares and green triangles
# plt.plot(years, colorado, "--", color='red', label="Colorado")
# plt.plot(years,connecticut, "s", color='blue', label="Connecticut")
# plt.plot(years,delaware,color='green',label='Delaware')
#
# # legend
# # https://matplotlib.org/users/legend_guide.html
# plt.ylim(ymin=0)  # Set's y axis start to 0.
# plt.legend(loc='center left')
# plt.xlabel("Year")
# plt.ylabel("Population")
# plt.title('Population by State')
#
# plt.show()

#EXCERCISE 7

# import matplotlib.pyplot as plt

# Plot scatter of x and y coordinates.
# time_X    = [0.1, 0.2, 0.3, 0.4, 0.5, 0.2]
# growth_Y  = [0.1, 0.15, 0.4,  0.6, 0.44, 0.17]
# plt.scatter(time_X, growth_Y, color='green', label='Bacteria A')

# Add a legend, axis labels, and title.
# plt.legend()
# plt.xlabel("Time (Hours)")
# plt.ylabel("Growth")
# plt.title('Bacteria Growth Over Time')
# plt.show()

#Excercise 8
# poundsA  = [120, 110, 160]
# inchesA  = [50, 48, 68]
# poundsB  = [121, 108, 150, 121, 121, 146]
# inchesB  = [49, 45, 85, 46, 50, 85]
#
# plt.scatter(poundsA,inchesA,color='orange',label='Student Region A')
# plt.scatter(poundsB,inchesB,color='green', label='Student Region B')
#
# plt.legend(loc='upper left')
# plt.xlabel('Wight(pounds)')
# plt.ylabel('Height(inches)')
# plt.title('Height vs Weight for Student Region A and B')
# plt.show()

#Excercise 9
# import matplotlib.pyplot as plt
# import numpy as np
#
# NUM_MEANS     = 5
# NUM_GROUPS    = 3
# bc_means      = [20, 35, 30, 35, 27]
# alberta_means = [25, 32, 34, 20, 25]
# saskatchewan_means = [18, 28, 32, 24, 31]
#
# # This generates indices from 0 to 4 in a format that is accepted for
# # plotting bar charts.
# ind = np.arange(NUM_MEANS)
# print(ind)
# width = 0.25
# plt.bar(ind[0], bc_means[0],width, label='BC')
# plt.bar(ind[0] + width,alberta_means[0],width,label='AB')
# plt.bar(ind[0]+width*2, saskatchewan_means[0],width, label='SK')
#
# plt.ylabel('Revenue')
# plt.title('Quarterly Revenue by Province')
#
# plt.xticks(ind + width / NUM_GROUPS, ('Q1', 'Q2', 'Q3', 'Q4', 'Q5'))
# plt.legend(loc='best')
# plt.show()

# Exercise 10
import pandas as pd
import matplotlib.pyplot as plt

# Import my own data into a DataFrame.

path = "../lab7/random_body_data.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age', 'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen', 'Waist', 'Hip', 'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))

plt.subplots(nrows=2,ncols=2,figsize=(14,7))

plt.subplot(2,2,1)
plt.hist(df['Pct.BF'],bins=10)
plt.xlabel('Pct.BF')
plt.ylabel('Frequency')

plt.subplot(2,2,2)
plt.hist(df['Age'],bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(2,2,3)
plt.hist(df['Weight'],bins=10)
plt.xlabel('Weight')
plt.ylabel('Frequency')

plt.subplot(2,2,4)
plt.hist(df['Height'],bins=10)
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()