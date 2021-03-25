# pdflatex

> Kompiliere eine LaTeX Quelldatei in ein PDF Dokument.
> Mehr Informationen: <https://linux.die.net/man/1/pdflatex>.

- Kompiliere ein PDF Dokument:

`pdflatex {{quelldatei.tex}}`

- Kompiliere ein PDF Dokument und gib ein bestimmtes Output-Verzeichnis an:

`pdflatex -output-directory={{pfad/zu/verzeichnis}} {{quelldatei.tex}}`

- Kompiliere ein PDF Dokument und stoppe bei jedem Fehler:

`pdflatex -halt-on-error {{quelldatei.tex}}`
