# Here is source code of the Python Program to remove the characters of odd index values in a string. The program output is also shown below.

def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=raw_input("Enter string:")
print("Modified string is:")
print(modify(string))