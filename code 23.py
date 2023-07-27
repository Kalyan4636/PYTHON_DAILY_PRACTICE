# Here is source code of the Python Program to form a new string made of the first 2 characters and last 2 characters from a given string. 
# The program output is also shown below.

string=raw_input("Enter string:")
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
print(new)