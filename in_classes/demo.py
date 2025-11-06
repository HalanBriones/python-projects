#First Class type of Variables
from time import process_time_ns

#String: '',"",""""""
print("String")
a="1"
b='2'
c="""3"""
d=a+b+c
print(type(a))
print(type(b))
print(type(c))
print(d)

#Multiplication
print("Multiplication")
a="Hello world"
print(a*5)

#Float
print('Float')
a=3.4
print(type(a))

#Boolean
print('Boolean')
isStudent = True
print(isStudent)

#Summary of Variables Int, Float, String, Bool

#To define a variable you can use only number, letter, _ (underscore)
#Dont allowed the number at the start of the variable
print('Camel Case')#second letter in upper case
#SNAKE is lastname_Firstname
firstName = "Halan" #camelcase is correct
lastName = "Briones"
print(firstName + lastName)
print(firstName,lastName)
print(firstName,lastName, sep="--")#add separation
print(firstName,end='*')
print(lastName)
print("Your full name is", firstName, lastName)

#INPUT()
#request string from client

firstName2 = input("What is your first name?: ")
print("Your first name is:",firstName2)

#casting is to convert to type of variable
#int(), float(), str()
print("Casting")
firstNumber=int(input("Insert number 1 :"))
secondNumber=int(input("Insert number 2 :"))
print(firstNumber+secondNumber)
