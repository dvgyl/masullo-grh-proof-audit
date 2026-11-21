# Spectral projections and normalization in a proposed trace formula for Hecke L-functions

[Second audit (PDF)](reports/second-audit/second-audit.pdf) · [Full verification dossiers (PDF)](reports/second-audit/verification-dossiers.pdf) · [Revised preprint (PDF)](reports/technical-audit.pdf)

This audit checks Alessandro Maria Masullo’s proposed proof of the Generalized Riemann Hypothesis. On p. 448 a compact test over an explicit quaternion number field gives a trace-class operator whose printed trace exceeds its actual trace by at least one. An elementary Gaussian example also contradicts the asymptotic formula on pp. 317–318. The audit identifies where the argument for GRH breaks down. Both examples are consistent with GRH.

The second audit gives full derivations, repairs, and corrections to the attribution of earlier objections. The dossiers distinguish contradictions to theorem statements from failures in their proofs. [Report source](reports/second-audit/REPORT.md) · [Dossier sources](reports/second-audit/notes/) · [Downloadable MathML edition](reports/second-audit/verification-dossiers.html) · [Preprint LaTeX](reports/technical-audit.tex) · [Projection supplement](reports/projection-counterexample.pdf)

## Results

| Manuscript reference | Result | Proof |
| --- | --- | --- |
| Thm. 6.3.2.1, pp. 304–307 | A test satisfying both moment conditions gives a strictly positive difference on the overlap where the proof requires equality. | Second audit §2.2 |
| Thm. 7.1.2.3, pp. 317–318 | A rational Gaussian orbit sum tends to two where the claimed bound tends to zero. | Second audit §2.2 |
| Thm. 10.4.3.5(3), pp. 472–473 | The output of convolution after spectral projection can lie outside the range of every proposed approximant. | Supplement pp. 1–3 |
| Thms. 11.2.1.2(2) and 11.2.1.4(2), pp. 488–489 | The missing right-hand geometric projection changes the strong limit on one vector. The scalar traces require a separate argument. | Supplement pp. 2–3 |
| Thm. 10.3.1.1(2), p. 448 | Over a specified quaternion field, the printed scalar trace exceeds the trace of a trace-class test operator by at least one. | Preprint §2 |
| Thm. 10.2.1.1, p. 440 and strip version pp. 445–446 | A cyclic cubic Hecke factor in an explicit degree-six field supplies actual repeated zeros for the divergent endpoint jet. | Supplement p. 4 |
| Lemma 10.4.2.5, pp. 461–462 | The lifting conclusion fails on a Hilbert space with uniformly bounded biorthogonal vectors. | Supplement p. 5 |
| Lemma 9.3.2.5, pp. 425–426 | Simple sparse pairs obstruct the claimed basis even after closing the convolution ideal. | Preprint §3 |
| Thm. 12.5.1.1, pp. 519–520 | Quadratic factorization and three fixed tests contradict the printed global normalization at any common strip width. | Preprint §§4–5 |

Page numbers refer to the 940-page manuscript dated 20 November 2026. Earlier work had already identified the p. 473 projection error and disproved the two pp. 488–489 operator limits in the arithmetic space. Section 2 credits those sources and gives an explicit all-width projection test. [Masullo’s manuscript](https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf) · [Earlier discussion of operator order](https://github.com/mccorvie/riemann-masullo/issues/2469#issuecomment-7057757877) · [Earlier endpoint and normalization objections](https://github.com/mccorvie/riemann-masullo/issues/2469#issuecomment-7057757662)

Manuscript SHA-256: `e039d3f6cf0a4b14f03c7edb85097752dd65c0a2fe543c76fe992be234f97bf5`.

## Reproduction

~~~sh
sha256sum -c SHA256SUMS  # Verify the distributed files
make check               # All six exact-arithmetic check scripts
make check-z3            # Three additional Z3 assertions
make pdf                 # Build the preprint and projection supplement in build/
make second-audit        # Rebuild the second audit and verification dossiers
~~~

The standard checks require Python 3. The three additional assertions use the native Z3 shared library. Building the reports requires Pandoc, pdfLaTeX, XeLaTeX, and DejaVu fonts. The scripts verify finite algebraic and arithmetic statements. The analytic arguments and their assumptions appear in the proofs. [Recorded check output](reports/second-audit/check-results.txt)

## Provenance

GPT 6.2 Astra generated the analysis, agent cross-checks, text, and code in Codex. [deyvium](https://github.com/dvgyl) directed the investigation and requested independent verification. The work has not undergone human peer review.
