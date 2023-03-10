#Here is source code of the Python Program to find the roots of an equation. The program output is also shown below.

print("Equation: ax^2 + bx + c ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=b**2-4*a*c
d1=d**0.5
if(d<0):
    print("The roots are imaginary. ")
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2))


#Program Explanation
# 1. User must enter the coefficients of the equations and store it in three separate variables.
# 2. The value value of the discriminant, d, is found out which determines the nature of roots of the equation.
# 3. If the value of the discriminant is lesser than 0, the roots are imaginary.
# 4. If the value of the discriminant is greater than 0, the roots aren’t imaginary.
# 5. The value of the roots is found out using the quadratic formula.
# 6. The roots of the equation are printed.