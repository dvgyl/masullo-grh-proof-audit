"""Exact arithmetic certificates for portions of the Chapter 6–8 audit.

Run python3 masullo-next-synthesis-checks.py. Optional --z3 checks the first
jet algebra and strip overlap with an installed native Z3 library. The Tate
identities, Fourier transform, continuity and topological claims are proved
in the accompanying report.
"""
from fractions import Fraction as F
import sys


def h_dyadic_probe(t):
    """Evaluate h at a (positive) multiple 2^k * 7/8.

    The bumps have radius 1/32 and centers 7/8 and 5/8, the first of height
    one. All dyadic translates of 7/8 except 7/8 itself miss both bumps.
    """
    center = F(7, 8)
    if t == center:
        return 1
    assert abs(t-center) > F(1, 32) and abs(t-F(5, 8)) > F(1, 32)
    return 0


def orbit_probe(t, units):
    positive_valuations = 0
    u = t
    while u <= 1:
        positive_valuations += h_dyadic_probe(u)
        u *= 2
    if units:
        return positive_valuations - h_dyadic_probe(t/2)
    return 2 * positive_valuations


def verify_z3():
    from ctypes import CDLL, c_char_p, c_void_p
    from ctypes.util import find_library
    path = find_library("z3")
    if not path:
        raise RuntimeError("--z3 requires a native Z3 library")
    lib = CDLL(path)
    lib.Z3_mk_config.restype = c_void_p
    lib.Z3_mk_context.argtypes = [c_void_p]
    lib.Z3_mk_context.restype = c_void_p
    lib.Z3_eval_smtlib2_string.argtypes = [c_void_p, c_char_p]
    lib.Z3_eval_smtlib2_string.restype = c_char_p
    lib.Z3_del_context.argtypes = [c_void_p]
    lib.Z3_del_config.argtypes = [c_void_p]
    cfg = lib.Z3_mk_config()
    ctx = lib.Z3_mk_context(cfg)
    try:
        script = b"""
(declare-const Z Real) (assert (> Z 0))
(push) (assert (= (* (- 1 (/ 1 4)) Z) (* (/ 1 4) Z))) (check-sat) (pop)
; First jet over C: write the first derivative of P*B in real/imaginary parts.
(declare-const pr Real) (declare-const pi Real)
(declare-const dpr Real) (declare-const dpi Real)
(declare-const br Real) (declare-const bi Real)
(declare-const dbr Real) (declare-const dbi Real)
(assert (= pr 0)) (assert (= pi 0)) (assert (= dpr 1)) (assert (= dpi 0))
(assert (= br 1)) (assert (= bi 0))
(define-fun jetReal () Real (+ (- (* dpr br) (* dpi bi)) (- (* pr dbr) (* pi dbi))))
(define-fun jetImag () Real (+ (* dpr bi) (* dpi br) (* pr dbi) (* pi dbr)))
(push) (assert (or (distinct jetReal 1) (distinct jetImag 0))) (check-sat) (pop)
; Gaussian at t=1/n^2: after exp(-y)>=1-y and pi<4, multiply by n^4.
(declare-const n Real) (declare-const C Real)
(assert (>= n 2)) (assert (<= C n))
(assert (<= (* 2 (- (* n n n n) 4)) (* C n n n))) (check-sat)
"""
        answers = lib.Z3_eval_smtlib2_string(ctx, script).decode("ascii").split()
        assert answers == ["unsat", "unsat", "unsat"], answers
        print("Z3 verified the overlap residual, first-jet algebra, and Gaussian lower-bound inequality.")
    finally:
        lib.Z3_del_context(ctx)
        lib.Z3_del_config(cfg)


def main():
    assert 1-2*F(1, 4) == F(1, 2)
    for units, t, expected in ((False, F(7, 4), -1), (True, F(7, 2), F(1, 2))):
        source = orbit_probe(t, units)
        translated = orbit_probe(t/2, units)
        assert source == 0
        value = source - F(1, 2)*translated
        assert value == expected
        print(f"units={units}, t={t}, U(t)={source}, U(t/2)={translated}, PV={value}")
    if "--z3" in sys.argv[1:]:
        verify_z3()


if __name__ == "__main__":
    main()
