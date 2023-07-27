#  Here is source code of the Python Program to determine how many times a given letter occurs in a string recursively. 
# The program output is also shown below.

def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string=raw_input("Enter string:")
ch=raw_input("Enter character to check:")
print("Count is:")
print(check(string,ch))