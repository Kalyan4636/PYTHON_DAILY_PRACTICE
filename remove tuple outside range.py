# Here is source code of the Python Program to remove all tuples in a list of tuples with the USN outside the given range. 

y=[('a','12CS039'),('b','12CS320'),('c','12CS055'),('d','12CS100')]
low=int(input("Enter lower roll number (starting with 12CS):"))
up=int(input("Enter upper roll number (starting with 12CS):"))
l='12CS0'+str(low)
u='12CS'+str(up)
p=[x for x in y if x[1]>l and x[1]<u]
print(p)

# Program Explanation
# 1. User must enter the upper and lower roll number.
# 2. The prefixes are then appended to the roll numbers using the ‘+’ operator to form the USN.
# 3. List comprehension is then used to find the USN’s within the upper and lower range.
# 4. The list containing USN’s in the given range is then printed.