# Here is the source code of the Python Program to print all numbers in a range divisible by a given number. 


 
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)

# Program Explanation
# 1. User must enter the upper range limit and the lower range limit.
# 2. Then the user must enter the number to be divided from the user.
# 3. The value of i ranges from the lower limit to the upper limit.
# 4. Whenever the remainder of the number divided by i is equal to 0, i is printed.