# python program to generate all gray codes using recursion.

def get_gray_codes(n):
    """Return n-bit Gray code in a list."""

    if n == 0:
        return['']
    first_half = get_gray_codes(n - 1)
    secound_half = first_half.copy()

    first_half = ['0' + code for code in first_half]
    secound_half = ['1' + code for code in reversed(secound_half)]


    return first_half + secound_half


n = int(input('Enter the number of bits: '))
codes = get_gray_codes(n)
print('All {}-bit Gray Codes:'.format(n))
print(codes)
