#reusable code
#function is def
'''
def cal_number(a,b):
    return a+b,a-b,a*b,a/b #return multiple values -> tuple()
    #result=a+b

plus, sub, multi, div = cal_number(2,4) #de-packaging
print(type(cal_number(2,4)))
print(plus)
print(sub)
print(multi)
print(div)
'''

#local variable vs global variable
'''
c=20
def cal_number(a,b):
    d=21
    return a+b+c
'''

#parameters
'''
def cal_number(a,b):
    return a+b

print(cal_number(2,4)) #positional arguments
print(cal_number(a=2, b=4)) #key words argument -dont mix them
'''

#DocString is formal comment type it has several parts triple quotes

#mix quotes
'''
firstName = "'Halan'" # backslash means skip the next for char 
print(firstName)
'''
#pass run code with no error

#Module vs Script both are python files

#Module collection of functions, classes and variables. Nothing is running
#Script python file that has executing code. It often imports code from modules

#import key word to import
'''
from module import * not good
from module import function ok
import module great
'''

#Main Function is the entry point for the program, to begin running there

import hello

 #call statement without this the funciont wont be executed