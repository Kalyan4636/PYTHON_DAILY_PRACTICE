# heart pattern
n = 4

# upper part of the heart
for i in range(n//2, n, 2):
    # print first spaces
    for j in range(1, n-i, 2):
        print(" ", end="")
    # print first number
    for j in range(i):
        print(j+1, end="")
    # print second spaces
    for j in range(1, n-i+1, 1):
        print(" ", end="")
    # print second number
    for j in range(i):
        print(j+1, end="")
    print()

# lower part
for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i*2):
        print(j+1, end="")
    print()