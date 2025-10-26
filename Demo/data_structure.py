#Data structure class

#Dicctionary, List an Tuples
#List and tuples you can use index

#Container/collection
#related data can be grouped together into a single variable

#tuple is immutable
'''
tup = ()
print(type(tup))
'''
from multiprocessing.managers import ListProxy
from typing import Tuple

#constructor is used to build an objetc and an object is unique even if they have the same size and values

#constructor str,int,float , etc
'''
list1 = [1,2,3,5]
tup1 = tuple(list1)
'''
tup = (1) #int value
tup2 = (1,) # tuple
print(type(tup))
print(type(tup2))

#TUPLES you can have access to the values but you cannot modify it
#if you wanna modify tuples you need to convert them into a list


#int, float
'''
a=2
b=a
b=3
print(a)
'''
#object
#how to make a copy
#.copy() / or slicing
#NEVER MODIFY ORIGINAL DATA
'''
arr = [1,2,3]
arr1 = arr
arr1[0] = 10
print(arr) #the value it change
'''
#Summary Tuples
#TUPLE IS ordered sequence of elements, duplicates are allowed, values cannot be modified (are immutable)


#LIST (can be a mix of different types of data) =  ARRAY (is only the same data type)
#how to make a list with brackets [], also use constructor list
#you have multidimension Array where you have to use doble brackets to have access to a list inside of a list x[0][6]
#Library Numpy

list1 = [11,12,1,1,1,2,3,4,5,6,7]
#add elements to the list (APPEND)
#append you can use another array
'''
list1.append(8)
print(list1)
'''
# + to add also but not (-) to delete a value
'''
list1 = list1+[9]
print(list1)
'''
#extend take only 1 parameter but you can pass a array with multiple values
#combine 2 arrays
'''
list1.extend([8,9]) #also you can pass another array
print(list1)
'''
#INSERT
'''
list1.insert(4,10) #you can choose where to insert, first parameter is the index where you wanna insert it
print(list1)
'''
#REMOVE you need to pass the value that you wanna remove
list1.remove(1) #if you have repeat it values just remove one if you want to remove all of them you need to use a loop
print(list1)
#INDEX used for string and array / find only for string
arr = [1,2,3,4]
print(arr.index(1)) #give you the index where the value is positioned
#POP remove the last element or also can delete element base on index
arr2 = [1,2,3,4]
print(arr2.pop(2)) #2 is the index number
print(arr2)
#Delete remove(value)
arr3 = [1,2,3,4]
del arr3[2]
print("Array 3 ",arr3)
#SORT THE ARRAY
arr3 = [1,2,3,4]
#reverse give you the reverse of the array

#Usefull for the LAb
#sum, min, max with numbers but also alfabethic

#List comprehension = less code/ code reduction WILL ASK SOME QUESTION FOR THIS
#[expresion-loop-conditions] all in one line with brackets because the result will be an array

#SET set only store a unique value you can create one using set() or braces {}
#you cannot access to the values with index
#no repeat values
#you can use in to find values in the set
#you cannot change items but you add or remove items
#.add() / .update() / .remove() / .discard() (dont show errors)
#.clear() empties the set
# del will delete the set completely
# .union() combine two set together will delete the duplicates elements

#DICTIONARIES create using {} structure is key:value
#Dictionary can have duplicate values but not keys keys are unique

'''

Diferences between data structure
                Syntax definition   \  Mutable values   \ Allows duplicates         \   Index Access    \    
List   -->my_list = [1,2,3]         values can change       yes                             Yes
Tuple  -->my_tuple = (1,2,3)        cannot change           yes                             yes
Set    --> my_set = {1,2,3}         only add and remove     No                              No
Dictionary->my_dictionary = {'a':1, values can change       unique keys, can have           Access by key
                            'b':2,                              duplicate values
                            'c':3}

'''

a = [1,2,3]
b=a
a[0]=0      #this happens because list arrays doing this they reference an address position in memory
print(b)