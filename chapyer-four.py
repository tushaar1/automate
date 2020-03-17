# chapter 4: lists
# lists and tuple - can contain multiple values lists can contain
# other lists and this data can be arranged

# list data type 
# list is a value that contains multiple values in an ordered sequence
# list value refers to the list itself not the values in the list

# list value example
example = ['cat', 'dog', 'bat', 'pig']
# values inside the list are called items, seperated by commas 

# [] - empty list 
# indvidual values from lists
# lists are indexed so doing listName[n] will pull the needed item

# indexing for lists with multiple lists
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])  # first list 
print(spam[0][1])  # first list item 2
print(spam[1][4])  # second list item 5

# negative indexes 
# [-1] refers to the last index in the list -2 is the second to last etc.

# getting sublists with slices
# a slice can get several values from a list
spam1 = [10, 20, 30, 40, 50]
spam1[2]  # a list with an index 
spam1[1:4]  # a list with a slice 
print(spam1[0:-1])
# this will print all the values except the last one
# [x, y, z]  
# x - start point
# y - end point
# z - skipping 
# :y - from start till y - 1
# x: from x till end of list
# : - the whole list 

# getting a length of list 
len(spam)

# changing values of lists

"""
spam[0] = 'hello world
set a list index = to the new value 
you can also do 
spam[0] = spam[1] etc
"""

# list concatenation and list replication 
# + can combine two lists to make a new list value 
# * can be used to replicate a list like a string 

numberlist = [1, 2, 3, 4]
alphabet = ['a', 'b', 'c', 'd']
numandalph = numberlist + alphabet
print(numandalph)

print(alphabet * 3)

# removing values
"""
use del to delete values
del spam[2] - delete the third value in the list spam
or del spam - delete the whole list
"""

# lists is a good way to enter values into a database 
catNames = []  # create an empty list 
while True:  # while loop 
    print('Enter the name of cat ' +str(len(catNames) + 1) +' (Or enter nothing to stop.):') 
    name = input()  # add a name
    if name == '':  # break loop condition 
        break
    catNames = catNames + [name] # list concatenation  # create the list add the name 
print('The cat names are:')
for name in catNames:  # for loop to print out the names of the cat 
    print('  ' + name) 

# loops with lists 
# for loops can repeat the block of code for each value in a list

for i in range(4):
    print(i)
# basic for loop 

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for supply in range(len(supplies)):
    print('index ' +str(supply) + ' in supplies is ' + supplies[supply])

# how to use a forloop over a list
# for i in range(len(list))

# in and not in operators
# used to determine if a value is in a list using: in
# or not in the list using: not in
# these are basically Boolean values 


spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' in spam)
print('hey there' not in spam)

# multiple assignment in lists
cat = ['fat', 'black', 'loud']
size, color, disposition = cat

# augmented assignment 
spam = 42
spam = spam + 1
# same as
spam += 1

spam = spam - 1
# same as
spam -= 1

spam = spam * 1
# same as
spam *= 1

spam = spam / 1
# same as
spam /= 1

spam = spam % 1
# same as
spam %= 1

# these += and *= also do concatenation 
