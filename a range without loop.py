def printno(upper):
    if (uppper>0):
        printno(upper-1)
        print(uppeer)
upper=int(input("Enter upper limit: "))
printno(upper)

# PROGRAM EXPLANATION
# 1. user must enter the upper limit of the range.
# 2. This value is passed as an argument for the recursive function.
# 3. The base case for the recursive function is that the no. should always be greater than 0.
# 4. if no. is greater than 0,function is called again with argument as the number minus -1.
# 5. the number is printed.
# 6. the recursion contains continues until the number becomes lesser than 0.
