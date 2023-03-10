# Here is the source code of a Python program to test Collatz conjecture for a given number. The program output is shown below.

def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    print(1, end='')
 
 
n = int(input('Enter n: '))
print('Sequence: ', end='')
collatz(n)

# Program Explanation
# 1. The user is asked to input n.
# 2. The sequence is printed by calling collatz on n.