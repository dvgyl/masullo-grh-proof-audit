# Audit of Masullo's proposed proof of the Generalized Riemann Hypothesis

This repository checks *The Music of the Primes*, the 940-page manuscript by Alessandro Maria Masullo (dated 20 November 2026) that proposes a proof of the Generalized Riemann Hypothesis (GRH). It gives explicit counterexamples to theorems and proof steps that the argument depends on, together with exact-arithmetic checks that anyone can rerun.

**Conclusion.** The manuscript does not prove GRH as written. Several intermediate theorems are false, and the main trace identity (Theorem 12.5.1.1) fails with the Haar measure printed in the manuscript. None of this contradicts GRH itself. Every counterexample is consistent with GRH, and a correctly normalized version of the main identity at arbitrarily narrow widths would still imply GRH (preprint §13). The problem is in the proof, not in the conjecture.

## Documents

| Document | Contents |
| --- | --- |
| [Preprint](paper/preprint.pdf) ([LaTeX](paper/preprint.tex)) | The main paper, 16 pages. It covers the spectral projection, the false scalar trace, the sparse-pair basis obstruction, the normalization failure of the main identity and the remaining chapter-by-chapter findings. |
| [Projection supplement](paper/projection-supplement.pdf) ([LaTeX](paper/projection-supplement.tex)) | 5 pages. One explicit test that breaks the spectral projection at every strip width, plus the endpoint jet and lifting-lemma examples. |
| [Detailed report](report/report.pdf) ([Markdown](report/report.md)) | Longer derivations: the false trace value, Gaussian asymptotics, the finite-place natural boundary, results across Chapters 4–14 and the appendices, repairs, and attribution of earlier objections. |
| [Verification dossiers](dossiers/verification-dossiers.pdf) ([HTML](dossiers/verification-dossiers.html), [sources](dossiers/notes/)) | Six technical notes with complete proofs, exact hypotheses, alternative arguments and records of the public sources searched. |

Page and equation numbers refer to the 940-page manuscript dated 20 November 2026, [published here](https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf). Its SHA-256 is `e039d3f6cf0a4b14f03c7edb85097752dd65c0a2fe543c76fe992be234f97bf5`.

## Main results

| Manuscript reference | Result | Where |
| --- | --- | --- |
| Thm. 10.3.1.1(2), p. 448 | Over a specified quaternion number field, the printed scalar trace exceeds the actual trace of a trace-class test operator by at least one. | Preprint §2, Report §1 |
| Thm. 12.5.1.1, pp. 519–520 | Quadratic factorization over Q(√5) and three fixed tests contradict the printed global normalization at every common strip width. | Preprint §§4–5 |
| Thm. 10.4.3.5(3), pp. 472–473 | After spectral projection, convolution can send a vector outside the range of every proposed approximant. | Preprint §2, Supplement pp. 1–3 |
| Thms. 11.2.1.2(2) and 11.2.1.4(2), pp. 488–489 | The missing right-hand geometric projection changes the strong limit on one vector. The scalar traces need a separate argument. | Preprint §2, Supplement pp. 2–3 |
| Thm. 6.3.2.1, pp. 304–307 | A test that satisfies both moment conditions gives a strictly positive difference on the overlap, where the proof requires equality. | Report §2.2 |
| Thm. 7.1.2.3, pp. 317–318 | A rational Gaussian orbit sum tends to 2 where the claimed bound tends to 0. | Report §2.2 |
| Thm. 10.2.1.1, p. 440, and strip version, pp. 445–446 | A cyclic cubic Hecke factor in an explicit degree-six field gives actual repeated zeros for the divergent endpoint jet. | Preprint §2, Supplement p. 4 |
| Lemma 10.4.2.5, pp. 461–462 | The lifting conclusion fails on a Hilbert space with uniformly bounded biorthogonal vectors. | Preprint §2, Supplement p. 5 |
| Lemma 9.3.2.5, pp. 425–426 | Simple sparse pairs of zeros block the claimed basis even after the convolution ideal is closed. | Preprint §3 |

Earlier public work had already found the p. 473 projection error and disproved the two operator limits on pp. 488–489. The papers credit these and other prior objections where they overlap. See preprint §14 and the report's final section.

## Repository layout

```
paper/      preprint.tex/.pdf, projection-supplement.tex/.pdf
report/     report.md and report.pdf (detailed report)
dossiers/   notes/*.md (six technical notes), build.py, verification-dossiers.pdf/.html
checks/     check_*.py (exact-arithmetic checks), expected-output.txt
Makefile    check, build and checksum targets
SHA256SUMS  checksums of every tracked file
```

## Reproduce

```sh
sha256sum -c SHA256SUMS   # verify the distributed files
make check                # run the six exact-arithmetic check scripts
make check-z3             # three extra Z3 assertions (pip install z3-solver)
make pdf                  # rebuild paper/*.pdf from LaTeX
make report               # rebuild report/report.pdf
make dossiers             # rebuild the verification dossiers
```

The checks need only Python 3 and use exact integer and rational arithmetic. Compare their output with [checks/expected-output.txt](checks/expected-output.txt). Building the documents needs pdfLaTeX, XeLaTeX, Pandoc and the DejaVu fonts. The scripts verify finite algebraic and arithmetic statements only. The analytic arguments are proved in the papers.

## Provenance

GPT 6.2 Astra generated the analysis, text and code in Codex. Claude Opus 5.5 checked and verified the proofs. [deyvium](https://github.com/dvgyl) directed the project. The work has not been peer reviewed by humans.
