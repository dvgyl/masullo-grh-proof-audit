"""Finite exact checks for the foundations supplement. No third-party dependencies.

The infinite natural-boundary proof and transform formulas are in the report.
These identities check discrete witnesses and the finite polynomial algebra.
"""
from fractions import Fraction
from math import factorial, prod


def real_poles(indices):
    return {-(2 * k) for upper in indices for k in range(upper + 1)}


def gamma_seed_order_at_even_point(shifts, point):
    # Gamma((s + a)/2) has a simple pole when (s + a)/2 is a nonpositive integer.
    return sum((point + a) <= 0 and (point + a) % 2 == 0 for a in shifts)


def check_filtration():
    smaller = (0, 2)
    larger = (1, 0)
    assert smaller < larger
    assert real_poles(smaller) - real_poles(larger) == {-4}
    assert [gamma_seed_order_at_even_point((4, 4), s) for s in (0, -2, -4)] == [0, 0, 2]


def check_polar_span():
    for degree in range(2, 9):
        orders = [
            gamma_seed_order_at_even_point((2,) * j + (0,) * (degree - j), 0)
            for j in range(degree)
        ]
        assert orders == list(range(degree, 0, -1))
    # Jets of exp(ts) for positive, distinct integer t. Rational coefficients
    # follow from Taylor's formula, and the determinant is Vandermonde.
    for t in range(1, 6):
        first_jet_matrix = [[1, 1], [0, t]]
        (a, b), (c, d) = first_jet_matrix
        assert a * d - b * c == t
    size = 5
    coeffs = [[Fraction(t**k, factorial(k)) for t in range(size)] for k in range(size)]
    for i in range(size):
        for r in range(i + 1, size):
            multiplier = coeffs[r][i] / coeffs[i][i]
            coeffs[r] = [a - multiplier * b for a, b in zip(coeffs[r], coeffs[i])]
    assert prod(coeffs[i][i] for i in range(size)) == 1


def check_lacunary_bound():
    for j in range(1, 9):
        k = 2**j
        valuation = 4**j
        assert valuation == k * k
        assert valuation - k > 0
        # k! <= k^k. After removing (log 2)^k, one term already has
        # normalized k-th derivative at least (k/2)^k.
        coeff = Fraction(valuation**k, 2**k * factorial(k))
        assert coeff >= Fraction(k, 2) ** k
        for r in range(j + 1):
            assert valuation % 4**r == 0


if __name__ == "__main__":
    check_filtration()
    check_polar_span()
    check_lacunary_bound()
    print("Verified exact pole sets, gamma orders, dilation jets and lacunary lower bounds.")
