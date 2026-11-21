"""Exact finite checks for the contour and split-prime examples.

The general estimates for all n and the convergence claims are proved in
dossiers/notes/appendices.md. This script verifies finite arithmetic only.
"""
from fractions import Fraction


def contour_example(n):
    epsilon = Fraction(1, 2 ** (4 * n * n))
    amplitude = 2 ** (2 * n * n)

    assert 0 < epsilon < Fraction(3, 4)
    # log 2 < 1. Thus the phase is < 1/2, with cos(phase)>1/2.
    assert 2 * n * epsilon < Fraction(1, 2)
    # Ensures t^2 <= n^2+1 for |t-n| <= epsilon.
    assert 2 * n * epsilon + epsilon**2 < 1
    assert amplitude * epsilon == Fraction(1, 2 ** (2 * n * n))
    for offset in (0, epsilon / 2, epsilon):
        magnitude = 2 * amplitude * epsilon / (offset**2 + epsilon**2)
        assert magnitude >= amplitude / epsilon
    # Interval length 2 epsilon times the lower bound of the integrand.
    integral_bound = 2 * epsilon * amplitude / epsilon / 2 ** (n * n + 1)
    assert integral_bound == 2 ** (n * n)


def split_prime_example():
    # The ring of integers has generator (1+sqrt(5))/2.
    roots = [r for r in range(11) if (r * r - r - 1) % 11 == 0]
    assert roots == [4, 8]
    assert 4 * 4 % 11 == 5


if __name__ == "__main__":
    for index in range(2, 21):
        contour_example(index)
    split_prime_example()
    print("19 exact pole-pair checks and the split-prime check passed.")
