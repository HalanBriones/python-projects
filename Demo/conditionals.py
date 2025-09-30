#Conditionals
#IF elif else
# Relational Operators are <,<=,==, >=, >
#Logical Operators !=, &&? , ||?, &, |
#Try and Except
#Is used in case you know part of your code can blow up to avoid that you use the part EXCEPT
# in the way that your program won't stop if that part of the code don't go well
#Example Try - Except
'''num = input("Insert a number: ")
try:
    a = int(num)
except:
    a = -1

if a > 0:
    print("You insert a number succesfully and your number is: ", a)
else:
    print("Not a number")
'''

#True: None; Number(+,-), String
#False: 0
'''
inputValue = input("type True or False: ").upper() #also lower()
if(inputValue=="TRUE"):
    print("Good")
else:
    print("Bad")
'''
'''
#Function
def compare_values(a,b):
    if(a>b):
        return 1
    else:
        return 0


if(compare_values(4,3)):
    print('Yes')
else:
    print('No')
'''

#print(type(2>=3)) #return boolean

finalGrade = int(input("What is your final Grade? : "))
if finalGrade > 100 or finalGrade<0:
    print("Invalid grade")
else:
    if finalGrade >= 90:
        print("You got an A")
    elif finalGrade >= 80:
        print("You Got a B")
    elif finalGrade >= 70 :
        print("You got a C")
    elif finalGrade >= 60 :
        print("You got a D")
    elif finalGrade < 60 :
        print("You got a F")