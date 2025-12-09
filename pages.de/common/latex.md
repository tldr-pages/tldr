# latex

> Kompiliere eine LaTeX Quelldatei in ein DVI Dokument.
> Weitere Informationen: <https://texdoc.org/serve/tex.man1.pdf/0>.

- Kompiliere ein DVI Dokument:

`latex {{quelldatei.tex}}`

- Kompiliere ein DVI Dokument und gib ein bestimmtes Output-Verzeichnis an:

`latex -output-directory={{pfad/zu/verzeichnis}} {{quelldatei.tex}}`

- Kompiliere ein DVI Dokument und stoppe bei jedem Fehler:

`latex -halt-on-error {{quelldatei.tex}}`
