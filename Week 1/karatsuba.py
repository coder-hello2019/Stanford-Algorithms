"""
Implementation of Karatsuba multiplication

Assume that:
    * n is a power of 2
    * x and y are positive (to achieve a straightforward way of determining the length of the digits)
"""

def karatsuba(x, y):
    n = max(len(str(x)), len(str(y)))

    midpoint = n//2
    # base case: return product of nums if they are 1 digit long
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x*y
    else:
        # split up the input nums into required components
        a = x // 10**(midpoint)
        b = x % 10**(midpoint)
        c = y // 10**(midpoint)
        d = y % 10**(midpoint)

        # p = a + b
        p = a + b
        # q = c + d
        q = c + d

        # recursively call karatsube on ac, bd and pq
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        pq = karatsuba(p, q)

        # compute final result according to formula
        abdc = pq - ac - bd
        result = ac * 10 ** (midpoint*2) + (10 ** midpoint * abdc) + bd

        return result

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
