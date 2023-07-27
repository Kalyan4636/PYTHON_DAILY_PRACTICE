# Here is source code of the Python Program to remove the nth index character from a non-empty string. The program output is also shown below.

def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
string=raw_input("Enter the sring:")
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))