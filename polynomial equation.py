# Here is source code of the Python Program to compute a polynomial equation given that the coefficients of the polynomial are stored in a list.

import math
print("Enter the coefficients of the form ax^3 + bx^2 + cx + d")
lst=[]
for i in range(0,4):
    a=int(input("Enter coefficient:"))
    lst.append(a)
x=int(input("Enter the value of x:"))
sum1=0
j=3
for i in range(0,3):
    while(j>0):
        sum1=sum1+(lst[i]*math.pow(x,j))
        break
    j=j-1
sum1=sum1+lst[3]
print("The value of the polynomial is:",sum1)

# Program Explanation
# 1. The math module is imported.
# 2. User must enter the coefficients of the polynomial which is stored in a list.
# 3. User must also enter the value of x.
# 4. The value of i ranges from 0 to 2 using the for loop which is used to access the coefficients in the list.
# 5. The value of j ranges from 3 to 1, which is used to determine the power for the value of x.
# 6. The value of the first three terms is computed this way.
# 7. The last term is added to the final sum.
# 8. The final computed value is printed.