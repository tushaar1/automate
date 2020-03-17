def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    elif number % 2 == 1:
        print( 3 * number + 1)
        return 3 * number + 1
n = input('Give me a number: ')
while n != 1:
    n = collatz(int(n))
no = 2
no % 2 == 0 # even
no % 2 == 1 # odd