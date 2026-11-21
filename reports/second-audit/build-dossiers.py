"""Build the verification dossiers from the six local Markdown sources."""
from pathlib import Path
import re
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parent
CHAPTERS = [
    ("foundations", "Finite-place tests and the second structure theorem"),
    ("synthesis", "The converse theorem, asymptotics and spectral jets"),
    ("existing-spectral", "Mellin quotients and the spectral trace"),
    ("existing-trace", "The geometric trace and the endgame"),
    ("appendices", "Contour shifts and auxiliary claims"),
    ("crosscheck", "Independent verification and public provenance"),
]


def combine_notes():
    document = ['---\ntitle: "Verification dossiers"',
                'subtitle: |\n  Companion to the second audit of The Music of the Primes  \n  *GPT 6.2 Astra prepared these mathematical verification notes.*',
                'date: "21 November 2026"\n---\n']
    for slug, title in CHAPTERS:
        path = ROOT / "notes" / f"masullo-next-{slug}.md"
        body = path.read_text().splitlines()[1:]
        document.extend(["# " + title, "", *body, ""])
    # Pandoc's MathML writer uses modern LaTeX font commands.
    return re.sub(r"\{\\rm\s+(\w+)\}", r"{\\mathrm{\1}}", "\n".join(document))


def build():
    document = combine_notes()
    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp) / "dossiers.md"
        md.write_text(document)
        shared = ["pandoc", str(md), "--from=markdown+tex_math_single_backslash",
                  "--toc", "--toc-depth=1", "--metadata", "lang=en"]
        subprocess.run([*shared, "--standalone", "--mathml", "--embed-resources",
                        "--css", str(ROOT / "dossiers.css"), "-o",
                        str(ROOT / "verification-dossiers.html")], check=True)
        # Preserve the digits while giving the typesetter a break inside long hashes.
        print_text = re.sub(r"`([0-9a-f]{32})([0-9a-f]{32})`",
                            lambda m: f"`{m[1]}` `{m[2]}`", document)
        md.write_text(print_text.replace("≪", r"\(\ll\)"))
        subprocess.run([*shared, "--pdf-engine=xelatex", "--top-level-division=chapter",
                        "-V", "documentclass=report", "-V", "papersize=a4",
                        "-V", "geometry:margin=24mm", "-V", "fontsize=11pt",
                        "-V", "mainfont=DejaVu Serif", "-V", "monofont=DejaVu Sans Mono",
                        "-o", str(ROOT / "verification-dossiers.pdf")], check=True)


if __name__ == "__main__":
    build()
