# Here is source code of the Python Program to find the binary equivalent of a number without using recursion. The program output is also shown below.

n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")