# to form an integer that has number of digit at 10's place & LSD at 1's place.
#code_with_kalyan_

n=int(input("Enter the number: "))
temp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(tmp)
c=str(k)
d=c+b[k-1]
print("The new number formed:",int(d))
