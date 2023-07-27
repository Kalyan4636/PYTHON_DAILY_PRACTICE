#Here is source code of the Python Program to add a key-value pair to a dictionary. The program output is also shown below.

key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)