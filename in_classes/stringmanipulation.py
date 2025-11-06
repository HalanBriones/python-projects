#find() funtion used to find the first ocurrence of the specified value return -1 if values is not found
#syntax string.find(value, start, end)
sentence = "A lazy dog jumped over log"
print("Starting position: "+str(sentence.find('dog'))) #7
print("Starting position:"+str(sentence.find('cat'))) #-1

#Slicing syntax format string[start:end] from start up to but not including, end
fullName="Halan Briones"
spacePosition = fullName.find(" ")
starPosition=0
endPosition = spacePosition
firstName= fullName[starPosition:endPosition]
lastName = fullName[spacePosition+1:]
print(firstName)
print(lastName)

#replace() exchange old text and with new text
newSentence = sentence.replace("dog",'cat')
print(newSentence)

#split() separate a string on preferred delimiter
sentenceList = sentence.split(' ')
print(sentenceList)

#join() opposite compared with split function, convert an array back to a single string
delimiter = ' '
backtostring = delimiter.join(sentenceList)
print(backtostring)



#Scope and Precedence
#Scope refers to the region where the variable is defined a variable only exist in the region where it is defined.
#When 2 variables have the same name the variable with the most localized scope is the one that is recognized.
#This bias to recognize local variables over global variables is called precedence
def displayContent(x): #x=a; x->100
    a = 25 # The number is born here.
    print('Inside the function the variable \'a\'=' + str(a))
    print('The parameter x=' + str(x))
    return # Locally declared variables die here when the function exits.
a = 100
displayContent(a)
print("The global value for \'a\'=" + str(a))

#Visualization process of converting raw data into easily understood pictures of information that enable effective decisions

#Line Graphs connect individual data points with lines. It's usually used to show trends over continuos variable
#Example in the PDF of the class number 8

#Scatter Plots show how one variable is correlated to another for multiple samples
#Used to visualize the relationship between two numeric variables or show the distribution of individual data points
#Example in PDF of the class number 8

#Bar Plots, represent categorical data with rectangular bars with lengths proportional to the values that they represent
#Shows comparison among discrete categories
#barh() make a horizontal
#Examples in the PDF of the class number 8

#Grouped Bar Plots
#Examples in the PDF of the class number 8

#Frequency Histograms
#Tables with precise frequency and ranges is helpful. However, many numbers in summary report can be overwhelming
#So histograms offer a quick but effective overview of frequency, range and distribution
#Examples in the PDF of the class number 8

#Display Multiple Graphs, explatory data analisys(EDA) and reporting will be often need to represent summaries about many variables
#You can adjust graphics output so more than one chart appears in the same row
#plt.subplots(nrows=2, ncols=3, figsize=(3,4))
#Examples in the PDF of the class number 8

