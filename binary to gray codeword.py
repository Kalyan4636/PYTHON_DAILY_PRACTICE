# python program to convert binary to gray codeword.

def binary_to_gray(n):
    """convert Binary to Gray codeword and return it."""
    n = int(n, 2)# convert to int
    n >= (n >> 1)

    #bin(n) return n's binary representation with a '0b' prefixed
    #the slice operation is to remove the prefix
    return bin(n)[2:]

g =input('Enter binary number: ')
b = binary_to_gray(g)
print('Gray codeword:' , b)
