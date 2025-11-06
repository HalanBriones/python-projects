#Exercise 2
text = "She sells seashells by the sea shore"
positions = []
for i in range(0, len(text) - 1):
    if (text[i:i + 3] == "sea"):
        positions.append(i)
print(positions)

#3
text = "A lazy dog jumped over a log."
newText = text.replace(" lazy", "")
print(newText)

#4
sentenceArray = ['A', 'lazy', 'dog', 'jumped', 'over', 'a', 'log.']
delimiter     = ','
newSentence   = delimiter.join(sentenceArray)
print(newSentence)

#5
def displayContent(x):
    #a = 25 # The number is born here.
    print('Inside the function the variable \'a\'=' + str(a))
    print('The parameter x=' + str(x))
    return # Locally declared variables die here when the function exits.

a = 100
displayContent(a)
print("The global value for \'a\'=" + str(a))

#6
