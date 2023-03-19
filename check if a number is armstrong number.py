n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("Enter number is an armstrong number: ")
else:
    print("Enter number isn't an armstrong number: ")