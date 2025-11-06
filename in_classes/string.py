
#   csv, json

#Pass arguments to the program itself
#AKA Command line parameters
'''
import sys

def main():
 if len(sys.argv) <= 2:
    print("Not enough command line arguments")
    exit(0)
 elif len(sys.argv) > 3:
    print("Too many command line arguments")
    exit(0)
print("Hello, %s, %s" % (sys.argv[1], sys.argv[2]))

if __name__ == "__main__":

'''

#String methods, indexing and slicing
#you can have access individual characters using indexing (+/-)
#slicing is used to change individual character of a string
#String are ordered sequences
#\t tab, four spaces to the side \n jump to next line
# \ to use to print or use special characters
# is used to join (concatenate strings)
# asterik(*) is used to repeat the string
#print("atm".center(40))

#formating a string
def main():
    name="Bob"
    quantity = 10
    prince= 10.99
    message = "%s purchased %d socks for %.3f $ for each"%(name, quantity,prince)
    print(message)
    '''
    %d integer 
    %s string 
    %f float
    %.<number of digits>f floating point numbers with fixed amount of digits to the right of the dot
    %x%X integers in hex representation (lower case/upper case)
    %e/%E floating points in exponential format(lowercase/uppercase) ex: 1.7e3
    '''

#f-string
def main2():
    name = "Bob"
    quantity = 10
    prince = 10.99
    message = f"{name} purchased {quantity} socks for {prince} $ for each"
    print(message)

#another way is "{} purchased {} socks for {} $ for each".format("bob",10, prince)

#DATA FORMATS CSV = coma separate values common use with spreadsheets
#DATA FORMAT JSON = javascript object notation consist of arrays, objects and key/value pairs common use with web-based interfaces

#String INDEX
firstName= "Halan"
print(len(firstName))

for i in range(len(firstName)):
    print(str(i)+" ----->"+firstName[i])

#String Slicing
#[start:up to:steps]
# [:] start = 0 and up to the whole lenght of the string
#don't modify the original data you cannot get it back
# always the start should be less than the up to
#if up to is larger that the start you will get an empty string
#if +:start < up to
#if :start > up to when the steps is negative
str = "This is a test!"
print(str[-1:])
print(str[0:4])
print(str[:4])
print(str[0:7])
print(str[:7])
print(str[10:14])
print(str[10:])
print(str[:-1]) #everything except the last up to but not include
print(str[::-1]) #reverse string

#split()
tokens = str.split()
print(tokens)

#join()
#message = tokens.join() #fixed
#print(message)

#replace
#str = str.replace("This","Halan")
#print(str)

#index() and find return to first occurence index
#find: string only
#index: string and array index retunr error if not find it
str1="Hello world world world"
str1=str1.count("world")
print(str1)

#in

word = "python"
print("a" in word)







