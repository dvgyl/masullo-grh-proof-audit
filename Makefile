REPORTS := technical-audit projection-counterexample
PDFS := $(addprefix build/,$(addsuffix .pdf,$(REPORTS)))

.PHONY: pdf check check-z3 second-audit

pdf: $(PDFS)

build/%.pdf: reports/%.tex | build
	pdflatex -halt-on-error -interaction=nonstopmode -output-directory=build $<
	pdflatex -halt-on-error -interaction=nonstopmode -output-directory=build $<

build:
	mkdir -p build

check:
	@set -e; for script in checks/*.py; do python3 "$$script"; done

check-z3:
	python3 checks/masullo-next-synthesis-checks.py --z3

second-audit:
	pandoc reports/second-audit/REPORT.md --from=markdown+tex_math_single_backslash \
	    --pdf-engine=pdflatex -V papersize=a4 -V geometry:margin=25mm -V fontsize=11pt \
	    -V colorlinks=true -V urlcolor=blue --number-sections -o reports/second-audit/second-audit.pdf
	python3 reports/second-audit/build-dossiers.py
