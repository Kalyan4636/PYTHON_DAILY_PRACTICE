# hollow triangle number pattern
n = 6
for i in range(1, n+1):
    count = 1
    for j in range(i):
        # print numbers only at the start and end of the row
        if j == 0 or j == i-1:
            print(count, end='')
            count += 1
        # print only numbers if it's last row
        else:
            if i != n:
                print(' ', end='')
            else:
                print(count, end='')
                count += 1
    print()