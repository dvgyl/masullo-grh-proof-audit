PAPERS := preprint projection-supplement
LATEX := pdflatex -halt-on-error -interaction=nonstopmode -output-directory=build

.PHONY: check check-z3 pdf report dossiers all checksums clean

# Run the six exact-arithmetic check scripts and print their output.
check:
	@set -e; for script in checks/check_*.py; do echo; echo "\$$ python3 $$script"; python3 "$$script"; done

# Optional SMT assertions (needs `pip install z3-solver` or a system libz3).
check-z3:
	python3 checks/check_synthesis.py --z3

# Build the preprint and the projection supplement, then copy them into paper/.
pdf:
	mkdir -p build
	@set -e; for p in $(PAPERS); do \
	    $(LATEX) paper/$$p.tex > /dev/null; \
	    $(LATEX) paper/$$p.tex > build/$$p.stdout || { cat build/$$p.stdout; exit 1; }; \
	    cp build/$$p.pdf paper/$$p.pdf; echo "built paper/$$p.pdf"; \
	done

# Build the detailed report (needs Pandoc and pdfLaTeX).
report:
	pandoc report/report.md --from=markdown+tex_math_single_backslash \
	    --pdf-engine=pdflatex -V papersize=a4 -V geometry:margin=25mm -V fontsize=11pt \
	    -V colorlinks=true -V urlcolor=blue --number-sections -o report/report.pdf

# Build the verification dossiers as PDF and HTML (needs Pandoc, XeLaTeX, DejaVu fonts).
dossiers:
	python3 dossiers/build.py

all: check pdf report dossiers checksums

checksums:
	git ls-files | grep -v '^SHA256SUMS$$' | sort | xargs sha256sum > SHA256SUMS

clean:
	rm -rf build
