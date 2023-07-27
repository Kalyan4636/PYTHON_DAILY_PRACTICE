# Here is source code of the Python Program to accept a hyphen separated sequence of words as input and print
#  the words in a hyphen-separated sequence after sorting them alphabetically. The program output is also shown below.

print("Enter a hyphen separated sequence of words:")
lst=[n for n in raw_input().split('-')]  
lst.sort()
print("Sorted:")
print('-'.join(lst))