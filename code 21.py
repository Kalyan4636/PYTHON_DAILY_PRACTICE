# Here is source code of the Python Program to count the number of lowercase characters and uppercase characters in a string. 
# The program output is also shown below.

string=raw_input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)