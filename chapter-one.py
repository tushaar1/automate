print('')
'''
operators:
** - exponent
% - modulus/remainder
// - integer division floored division
/ - division
* - multiplication
- subtraction
+ - subtraction
pemdas - order of operation

data types - category for values
integer - whole numbers
float - decimal point
strings - letters
'''

'''string concatenation'''
'''
+ with strings is when you add two different strings together
'''
# example
print('alice'+'bob')
# cant add string plus int
# muliply string
print('alice' * 5)

# variables
'''
a variable is when you give something a value
x = 10
x is the variable with the value of ten.
this can be changed whenever, a variable is initialised when you first give it a
value

variables have naming values too
cant start with a number
cant contain a space
only uses letters number and the _
they are case sensitive
'''
print('hello, world')
name = input('what is your name? ')
print('good to meet you '+ name)
print('the length of your name is: ')
print(len(name))
age = input('what is your age? ')
print('you will be ' + str(int(age) + 1) + ' in one year')

print()  # this creates a blank line
# input() waits for an input from the user
# len()  This gives the length of the string or a variable containg a strings
"""
str() - converts a variable or int into a strings
int() - converts a string or float into an integer
float() - converts an integer or string into a float
"""

# int stores all the text it gets as a string
# spaces matter in strings "hello" is different from "hello "

'''text and number equivalance'''

print(44 == '44')
print(44 == 44.0)
print(42.0 == 0042.000)

"""
It is good to remember the different types of operators 
(+, -, *, /, //, %, and ** for math operations
 + and * for string operations)
three data types 
(integers, floating-point numbers, and strings)
"""
msg = "hello world"
print(msg)

print(msg.capitalize())

print(round(99.95))
