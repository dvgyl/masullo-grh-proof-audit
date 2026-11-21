"""Exact finite checks accompanying the spectral dossier. Run with Python 3.

The general proofs, zero-counting inputs, and analytic trace-class arguments are
in dossiers/notes/spectral.md. Finite experiments alone cannot establish them.
"""
from fractions import Fraction
from math import factorial


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Fraction())


def plus(x, y):
    return tuple(a + b for a, b in zip(x, y))


def times(c, x):
    return tuple(c * a for a in x)


def block_checks(root):
    """Choose n a square so every vector entry is an exact rational."""
    n = root * root
    unit = [tuple(Fraction(i == j) for i in range(2 * n)) for j in range(2 * n)]
    d = tuple(Fraction(i < n, root) for i in range(2 * n))
    v = tuple(Fraction(i >= n, root) for i in range(2 * n))
    primal = [plus(e, v) for e in unit[:n]] + unit[n:]
    dual = unit[:n] + [plus(f, times(-1, d)) for f in unit[n:]]
    for i, x in enumerate(primal):
        assert dot(x, x) in (1, 2)
        for j, y in enumerate(dual):
            assert dot(x, y) == int(i == j)
    half = tuple(sum(dot(d, dual[j]) * primal[j][i] for j in range(n))
                 for i in range(2 * n))
    assert dot(d, d) == 1 and dot(half, half) == n + 1
    print(f"n={n}, squared halfway partial-sum norm on unit input = {n+1}")


def check_quaternion_regular_character():
    # Class order 1, -1, pair ±i, pair ±j, pair ±k. Four linear characters
    # annihilate the center. Degree-two irrep has values 2,-2,0,0,0.
    chars = [[1, 1, a, b, a * b] for a in (1, -1) for b in (1, -1)]
    chi = [2, -2, 0, 0, 0]
    dims = [1] * 4 + [2]
    regular = [sum(d * row[j] for d, row in zip(dims, chars + [chi])) for j in range(5)]
    assert regular == [8, 0, 0, 0, 0]
    sizes = [1, 1, 2, 2, 2]
    assert sum(s * a**2 for s, a in zip(sizes, chi)) == 8
    print("Quaternion regular character contains its degree-two character twice.")


def check_mellin_lower_bound():
    # log(2)>1/2, e<3. The n=4k^2 term bounds the absolute Taylor
    # coefficient below by (2k^2/9)^k/k!, hence by (2k/9)^k.
    for k in range(1, 40):
        assert Fraction(2 * k * k, 9)**k / factorial(k) >= Fraction(2 * k, 9)**k
    print("Valuation-tail Taylor coefficient rational bound verified for k=1,...,39.")


if __name__ == "__main__":
    for root in (1, 2, 3, 4):
        block_checks(root)
    check_quaternion_regular_character()
    check_mellin_lower_bound()
