# An audit of Masullo’s proposed proof of the Generalized Riemann Hypothesis

**Release 1.0.0 · 21 November 2026**

**[Read the unified preprint (PDF)](reports/technical-audit.pdf)** · [LaTeX source](reports/technical-audit.tex)

The [five-page supplement](reports/projection-counterexample.pdf) gives a fixed smooth test over the rational numbers that disproves the operator identification in Theorem 10.4.3.5(3), p. 473, for every positive strip width. The same test disproves two Paley–Wiener convergence assertions on pp. 488–489. Every approximating operator kills one specific vector for which the alleged limit is nonzero. The proofs use a classically known zero of zeta on the critical line and require no numerical information about its location or multiplicity.

The preprint also gives the sparse-pair counterexample to Lemma 9.3.2.5 and a three-test factorization contradiction to Theorem 12.5.1.1 under the printed normalization. The results establish failures in the supplied argument for GRH. The truth of GRH remains open.

## Guide to the findings

| Manuscript reference | Result | Proof |
| --- | --- | --- |
| Thm. 10.4.3.5(3), pp. 472–473 | The output of convolution after spectral projection can lie outside the range of every proposed approximant. | Supplement pp. 1–3 |
| Thms. 11.2.1.2(2) and 11.2.1.4(2), pp. 488–489 | The missing right-hand geometric projection changes the strong limit on one vector. The scalar traces require a separate argument. | Supplement pp. 2–3 |
| Thm. 10.2.1.1, p. 440 and strip version pp. 445–446 | A cyclic cubic Hecke factor in an explicit degree-six field supplies actual repeated zeros for the divergent endpoint jet. | Supplement p. 4 |
| Lemma 10.4.2.5, pp. 461–462 | The lifting conclusion fails on a Hilbert space with uniformly bounded biorthogonal vectors. | Supplement p. 5 |
| Lemma 9.3.2.5, pp. 425–426 | Simple sparse pairs obstruct the claimed basis even after closing the convolution ideal. | Preprint §3 |
| Thm. 12.5.1.1, pp. 519–520 | Quadratic factorization and three fixed tests contradict the printed global normalization at any common strip width. | Preprint §§4–5 |

Masullo recognizes failure of commutation on p. 458. Prior public discussion also distinguishes the two operator orders. The supplement gives an explicit arithmetic counterexample and identifies the later equations it contradicts. The endpoint integrability error and the normalization problem had also been reported. Earlier sources are cited in both reports. The public comparisons do not establish priority. [Discussion of operator order](https://github.com/mccorvie/riemann-masullo/issues/2469#issuecomment-7057757877) · [Alternative approach to the traces](https://github.com/mccorvie/riemann-masullo/issues/1169#issuecomment-7057208991) · [Endpoint and normalization](https://github.com/mccorvie/riemann-masullo/issues/2469#issuecomment-7057757662)

## Source version

The review concerns Alessandro Maria Masullo’s 940-page *The Music of the Primes*, dated 20 November 2026. Page numbers refer to that PDF. Its SHA-256 digest is recorded below. The package distributes the review and links to the primary source. [Manuscript PDF](https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf)

```text
e039d3f6cf0a4b14f03c7edb85097752dd65c0a2fe543c76fe992be234f97bf5
```

## Reproduce the checks

From the release root run the following commands on a system with Python 3.8 or later and GNU coreutils.

```sh
python3 checks/masullo-audit-checks.py
sha256sum -c SHA256SUMS
```

The Python program uses exact rational arithmetic and integer square roots. It verifies the volume enclosure, finite zero counts, shell-mask identity, a bound for the fixed bump, and finite instances of the block projection. The two reports give the proofs for all widths and all block sizes.

To rebuild the PDFs, run `make pdf` with GNU Make, pdfLaTeX and the TeX packages named in the source preambles installed. The build writes its output in `build/`. The shipped PDFs are in `reports/`. [Supplement source](reports/projection-counterexample.tex) · [Technical audit source](reports/technical-audit.tex)

## AI provenance and citation

The investigation, independent agent cross-checks, mathematical exposition, code, and packaging of this review were performed entirely by AI in Codex. The model attribution supplied for this release is **GPT 6.2 Astra**. The release contains no independent runtime attestation of the exact model identifier. Project contributor [deyvium (@dvgyl)](https://github.com/dvgyl) directed the investigation and requested the independent verification. The mathematical literature, the manuscript, and public objections cited here have their own authors. The review has not undergone human peer review.

Suggested citation: *An audit of Masullo’s proposed proof of the Generalized Riemann Hypothesis*, version 1.0.0, 21 November 2026. Entirely AI-generated review, attributed to GPT 6.2 Astra.

## Distribution

The folder contents can be used as the root of a GitHub repository. This is a local release package. Zenodo requires research grounded in human-conducted work and excludes AI tools from the creator and contributor fields. This entirely AI-generated review is ineligible for deposit in its current form. [Zenodo’s policy for depositors](https://support.zenodo.org/help/en-gb/13-policies/227-what-is-your-usage-policy-for-generative-ai-for-depositors)
