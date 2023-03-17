n=int(input())
inp1=list(map(int,input().slipt('')))
if(len(inp1)==n):
   n1=max(inp1)
   n2=min(inp1)
   n3=n1-n2
   print(n3)
else:
   print("invalid input")
   
