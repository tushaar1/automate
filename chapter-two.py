# flow control
# these are statements which decide which instuction to run
# under specific conditions

# Boolean values
# these are True or False values

spam = True 
print(spam)
print(not spam)

'''
comparison operators

== equal to
!= not equal to
< less than
> greater than
<= less than or equal to
>= greater than or equal to
'''

print(42 == 42)
print(42 == 49)
print(2 != 3)
print(2 > 3)

# == and!= work for any data types
print('hello' == 'Hello')
print('dog' != 'cat')
print('dog' == 'Dog')

# remember the logic statements i learned they work for this

print(True == (True * False))

# >, <, <=, >= only work with float and int

# == - equal to
# = - assignment

'''
Binary boolean operators
and or take two boolean values, binary operators
True if both values are true - and 

truth table

True and True True
True and False False
False and True False
False and False False

True or True True
True or False True
False or True True
False or False False
'''

"""
not operator

only one Boolena vlaue or expression, gives us the opposite
Boolean value
"""

print(not True)
print(not False)

# boolean values and operators can be mixed just like in logic 

"""
Flow control
start with a condition and then a block of code called a clause.

condtions are Boolean expressions 

the block of code is indented blocks and can contain other blocks 
"""

name = 'Gary'
password = 'Swordfish'

if name == 'Mary':
    print('hello Mary')
else:
    print('hello stranger')
if password == 'Swordfish':
    print('accesss granted')
else:
    print('wrong password')


"""
Flow control statement
if statements:
the if statement clause will excecute if the condtion is True 
else its skipped, False

if following statement is true, excecute the code else skip it

the if statement has the following:

if keyword 
a condition which will evaluate to True or False
a colon
indented block of code 

else statement:
    only executed if the if statement is false 
else keyword
colon
indented block of code

elif statement 
read as else if, follows an if or else statement 
if the previous code was False try this block of code 

elif keyword
condtion which evaluates True or False
colon
indented block of code 

“If the first condition is true, do this. 
Else, if the second condition is true, do that.
Otherwise, do something else.”
"""

name = 'Gary'
age = 13

if name == 'Alice':
    print('hi, alice')
elif age < 12:
    print('you are not alice kiddo')
else:
    print('you are not alice nor a little kid ')

'''
while loop statements

the code in a while clause will be excecuted as long as the 
while statement's condition is True

while keyboard
condition
colon
indented block of code
'''

spam = 0
while spam < 5:
    print('hello world')
    spam += 1

# if and while statements kind of work the same way with such things

# break statements
# a way for while loops to stop early, if it reaches a break statement
# it closes immediatly 

while True:
    print('please type your name')
    name = input()
    if name != 'your name':
        break
print('Thank you')

# continue statements
# like break they are used inside loops 
# when a program reaches continue the program jumps to the top
# and reevaluates the loop's condition

while True:
    print('who are you? ')
    name = input()
    if name != 'Joe':
        break
    print('hello, Joe. What is the password? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break
    else:
        continue
print('access granted')

# 0 and 0.0 and '' - empty strings are considered false

"""
for loops and range()
while loops keep looping while the condition is True 
for loops work for a certain number

for i in range(5):
    this will excecute 5 times

for keyworld
variable name
in keyword
range method 
colon
indented block of code 
"""

print('my name is')
for i in range(5):
    print('jimmy five times (' +str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print(total)

# range has a function where it will start and stop at certain number

for i in range(12, 16):
    print(i)

# range can be called in three arguments
# x,y are the start and end point, z is the step argument, every z

for i in range(0, 10, 2):
    print(i)
# will give number by intervals
# also works with negative

for i in range(5, -1, -1):
    print(i)

# 5 is start point, -1 is end point, goes every -1 

# can import cool libraries to help with other work

import random, sys, os, math
# can import multiple modules at once

for i in range(5):
    print(random.randint(0, 100))

"""
from import statement
from random import * 
this will make it so that we do not need the random prefix
"""

# sys.exit()

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
