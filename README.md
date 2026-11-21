# Spectral projections and normalization in a proposed trace formula for Hecke L-functions

[Read the preprint (PDF)](reports/technical-audit.pdf) · [LaTeX source](reports/technical-audit.tex) · [Projection counterexample (5 pages)](reports/projection-counterexample.pdf)

This preprint examines Alessandro Maria Masullo’s proposed proof of the Generalized Riemann Hypothesis. Its central example uses one smooth test over the rationals. Every operator in a proposed approximation sends its output into a closed spectral subspace, yet the claimed limit sends a particular vector outside that subspace. This invalidates the operator identification on manuscript p. 473. Whether differently ordered operators have equal scalar traces requires a separate argument.

## Results

| Manuscript reference | Result | Proof |
| --- | --- | --- |
| Thm. 10.4.3.5(3), pp. 472–473 | The output of convolution after spectral projection can lie outside the range of every proposed approximant. | Supplement pp. 1–3 |
| Thms. 11.2.1.2(2) and 11.2.1.4(2), pp. 488–489 | The missing right-hand geometric projection changes the strong limit on one vector. The scalar traces require a separate argument. | Supplement pp. 2–3 |
| Thm. 10.2.1.1, p. 440 and strip version pp. 445–446 | A cyclic cubic Hecke factor in an explicit degree-six field supplies actual repeated zeros for the divergent endpoint jet. | Supplement p. 4 |
| Lemma 10.4.2.5, pp. 461–462 | The lifting conclusion fails on a Hilbert space with uniformly bounded biorthogonal vectors. | Supplement p. 5 |
| Lemma 9.3.2.5, pp. 425–426 | Simple sparse pairs obstruct the claimed basis even after closing the convolution ideal. | Preprint §3 |
| Thm. 12.5.1.1, pp. 519–520 | Quadratic factorization and three fixed tests contradict the printed global normalization at any common strip width. | Preprint §§4–5 |

Page numbers refer to the 940-page manuscript dated 20 November 2026. The preprint distinguishes the explicit examples developed here from earlier public objections. [Masullo’s manuscript](https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf) · [Earlier discussion of operator order](https://github.com/mccorvie/riemann-masullo/issues/2469#issuecomment-7057757877) · [Earlier endpoint and normalization objections](https://github.com/mccorvie/riemann-masullo/issues/2469#issuecomment-7057757662)

Manuscript SHA-256: `e039d3f6cf0a4b14f03c7edb85097752dd65c0a2fe543c76fe992be234f97bf5`.

## Reproduction

```sh
make check               # Run exact arithmetic checks with Python 3.8+
make pdf                 # Build both PDFs in build/ with pdfLaTeX
sha256sum -c SHA256SUMS  # Verify the distributed files
```

The Python script checks the volume bounds, finite zero counts, and selected identities used in the proofs. The preprint gives the arguments for all strip widths and block sizes.

## Provenance

GPT 6.2 Astra generated the analysis, agent cross-checks, text, and code in Codex. [deyvium](https://github.com/dvgyl) directed the investigation and requested independent verification. The work has not undergone human peer review.
