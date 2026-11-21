"""Exact finite certificates accompanying the trace and CM-character audit."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, isqrt, prod


def square_free_representative(n):
    """Return the signed squarefree representative of a nonzero integer."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    p = 2
    while p*p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent % 2:
            sign *= p
        p += 1
    return sign*n


def volume_certificate():
    # log(phi) = asinh(1/2). The alternating Taylor terms decrease to zero.
    def partial(m):
        return sum((-1)**k * F(comb(2*k,k),4**k*(2*k+1)*2**(2*k+1))
                   for k in range(m))
    lower_log, upper_log = partial(30), partial(31)
    d = 10**18
    r = isqrt(5*d*d)
    lower = 2*lower_log/F(r+1,d)
    upper = 2*upper_log/F(r,d)
    assert F(430408940964,10**12) < lower < upper < F(430408940965,10**12)


def cm_certificate():
    n = 1254
    assert n == 2*3*11*19 and n % 8 == 6
    points = [(-1058,21896),(-912,25992)]
    for x,y in points:
        assert y*y == x*(x-n)*(x+n)
    kummer = [square_free_representative(x) for x in [-n*n,n]+[x for x,_ in points]]
    assert kummer == [-1,1254,-2,-57]
    for size in range(1,5):
        for indices in combinations(kummer,size):
            assert square_free_representative(prod(indices)) != 1
    print('Kummer rank certificate:',kummer,'has 16 distinct subset classes.')
    print('E_1254 is a sign-minus congruent-number twist (n mod 8 = 6).')


if __name__=='__main__':
    volume_certificate()
    print('Independent asinh-series certificate: 0.430408940964 < V < 0.430408940965.')
    cm_certificate()

# The numerator of the unitary angular fourth power at (2+i) is (2+i)^4.
def gaussian_multiply(z, w):
    a, b = z
    c, d = w
    return a*c - b*d, a*d + b*c


generator = (2, 1)
square = gaussian_multiply(generator, generator)
real_part, imaginary_part = gaussian_multiply(square, square)
assert (real_part, imaginary_part) == (-7, 24)
assert real_part**2 + imaginary_part**2 == 25**2 and imaginary_part != 0
print("At the two primes over 5 the distinct phases are (-7 +/- 24i)/25.")
