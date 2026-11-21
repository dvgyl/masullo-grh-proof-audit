"""Reproduce the arithmetic checks in the audit with Python's standard library.

Every assertion uses integers or rational arithmetic.  No zero tables, network
access, or floating-point routines are required.  Run with Python 3.
"""
from fractions import Fraction as Q
from math import isqrt


def sqrt5_interval(digits=24):
    scale = 10**digits
    lower = isqrt(5 * scale**2)
    return Q(lower, scale), Q(lower + 1, scale)


def positive_log_bounds(x, terms=28):
    """Bounds for log(x), x>1, using its atanh series and a geometric tail."""
    assert x > 1
    y = (x - 1) / (x + 1)
    partial_sum = sum(2 * y**(2*k + 1) / (2*k + 1) for k in range(terms))
    tail = 2 * y**(2*terms + 1) / ((2*terms + 1) * (1-y*y))
    return partial_sum, partial_sum + tail


def count_product_zeros(t):
    """Number of n>0 with t < n^(2/3) <= t+1; integer endpoints handled."""
    return isqrt((t+1)**3) - isqrt(t**3)


def main():
    root_lo, root_hi = sqrt5_interval()
    log_lo, _ = positive_log_bounds((1+root_lo)/2)
    _, log_hi = positive_log_bounds((1+root_hi)/2)
    vol_lo, vol_hi = 2*log_lo/root_hi, 2*log_hi/root_lo
    assert Q(430408940964, 10**12) < vol_lo < vol_hi < Q(430408940965, 10**12)
    print("Certified: 0.430408940964 < vol(C_F^1) < 0.430408940965 for F=Q(sqrt(5)).")
    for t, expected in [(100, 15), (10000, 150), (1000000, 1500)]:
        count = count_product_zeros(t)
        assert count == expected
        print(f"Canonical-product zeros in ({t}, {t+1}]: {count}")
    # The zero-width witness has D(0) equal to a positive weighted mean
    # of (1+t^2)^(-2). On the specified bump support, monotonicity gives
    # this rigorous enclosure without evaluating any transcendental function.
    lo, hi = Q(5, 4), Q(7, 4)
    lower_bound = 1 / (1 + hi**2)**2
    upper_bound = 1 / (1 + lo**2)**2
    assert 0 < lower_bound < upper_bound < Q(1, 4)
    print(f"Fixed bump: {lower_bound} < D_0(0) < {upper_bound} < 1/4.")

    # Use square block sizes so every coordinate of the test and projection
    # in the lifting example is rational. Evaluate the inner products.
    for k in (1, 2, 3, 5, 9):
        n = k**2
        z = [Q(1, k)] * n + [Q(0)] * n
        image = [Q(0)] * (2*n)
        for i in range(n):
            coeff = z[i]  # coefficient functional e_i
            image[i] += coeff
            for j in range(n):
                image[n+j] += coeff / k
        assert sum(t*t for t in z) == 1
        assert sum(t*t for t in image) == 1 + n
    print("Block projection: squared norms n+1 for n = 1, 4, 9, 25, 81.")

    # Second-variable support identity: membership in A_j implies membership
    # in A_(k+1), which implies membership in A_k if j>=k+1.
    for ak in (0, 1):
        for ak1 in range(ak + 1):
            for aj in range(ak1 + 1):
                assert (ak1 - ak) * aj == 0
    print("Verified the shell-mask identity for every possible membership triple.")


if __name__ == "__main__":
    main()
