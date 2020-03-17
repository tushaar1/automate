# chapter 3 : functions
# a function is like a mini program like print(), we create our own

def hello():
    print('howdy')
    print('howdy!!!')
    print('hello there')

hello()
hello()

"""
def hello():
    ^ this is the first statement which defines the function hello()
    here is the block of code, the body of the function, executed 
    when function is called
"""

# def statement with parameters
def hello(name):
    print('Hello ' + name)

# this function has an argument in the ()
hello('alice')
hello('bob')

# return value and return statements

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
       return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

"""
this function has a few parts
first we create a def with an arugment 
then it reads the number and gives us an answer

we used a random int to help with the fortune reading
"""

print(getAnswer(random.randint(1, 9)))

# dont even need to do the whole define a var and then calc.

""" the none value 
None - represents the absense of a value 
used for print() - returns a Null value 
"""

print('hello')
print('world')
print()
print('hello', end='')
print('world')
# this would go in one line, end='' good when you need to disable
# new line 

print('cats', 'dogs', 'mice')
# seperated by a space automatically 
# you can replace the defualt space with commas or anything 
print('cats', 'dogs', 'mice', sep=',')

# local and global scope 
# parameters and variables assigned in a called function are the
# the functions local scope 

# variables that are assigned outside all functions are global 
# one cannot be both local and global 
# code in global scope cannot use local variables
# local scope can access global variables
# functions local scope called use variables in any other local scope

"""
def spam():
    eggs = 31337
spam()
print(eggs)
# this will give an error since eggs is a local variable 
"""

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# this will print spam for eggs since that is the global var

""" exception handling"""

def spam(divideBy):
    return 42 / divideBy

# if you did spam(0) - this will give an error 

# exception handling in action 

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error: invalid argument')

# this wont crash the code just let us know its invalid 
# any errors in the try block of code will also be caught 


""" guess the number """

import random 
number = random.randint(1, 20)

print('I am thinking of a number between 1 and 20')

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < number:
        print('guess too low')
    elif guess > number:
        print('guess to high')
    else:
        break
if guess == number:
    print('good job, you gusessed the number in ' +str(guessesTaken) + ' guesses')


def collatz(number):
    if number / 2 == 0:
        return number // 2
    if number / 2 != 0:
        return 3 * number + 1

collatz(4)
collatz(7)
collatz(10)