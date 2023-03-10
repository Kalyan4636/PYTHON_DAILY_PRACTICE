# Here is the source code of a Python program to find whether a number is a power of two. The program output is shown below.

def is_power_of_two(n):
    """Return True if n is a power of two."""
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0
 
 
n = int(input('Enter a number: '))
 
if is_power_of_two(n):
    print('{} is a power of two.'.format(n))
else:
    print('{} is not a power of two.'.format(n))
# Program Explanation
# 1. The user is prompted to enter a number.
# 2. is_power_of_two is called on the number.
# 3. If the return value is True, the number is a power of two.