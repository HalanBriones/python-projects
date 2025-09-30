#While and For
#For example with array

'''
arr = [2,12,16,11,5,40,-1,15,0]
max = arr[0]

for x in range(1, len(arr)):
    if(arr[x] > max):
        max = arr[x]
print(max)
'''
#While example with functions if else, etc
def helloWorld():
    print("Hello World")
def welcome():
    print("Welcome")

while True:
    option=input("Options:\n[1]: Hello\n[2]: Welcome\n[3]: Stop\nYour option: ")
    if option=="1":
        helloWorld()
    elif option == "2":
        welcome()
    elif option == "3":
        print("Good bye")
        break
    else:
        print("Wrong option. Please try again")

#Range range(start, end, step) range is use in For cycles

print("Range example")

print(list(range(0,10,3)))

#Nested Loop is a loop inside of another loop