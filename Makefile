REPORTS := technical-audit projection-counterexample
PDFS := $(addprefix build/,$(addsuffix .pdf,$(REPORTS)))

.PHONY: pdf check

pdf: $(PDFS)

build/%.pdf: reports/%.tex | build
	pdflatex -halt-on-error -interaction=nonstopmode -output-directory=build $<
	pdflatex -halt-on-error -interaction=nonstopmode -output-directory=build $<

build:
	mkdir -p build

check:
	python3 checks/masullo-audit-checks.py
