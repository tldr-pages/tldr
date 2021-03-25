# latex

> Kompiliere eine LaTeX Quelldatei in ein DVI Dokument.
> Mehr Informationen: <https://www.latex-project.org>.

- Kompiliere ein DVI Dokument:

`latex {{quelldatei.tex}}`

- Kompiliere ein DVI Dokument und gib ein bestimmtes Output-Verzeichnis an:

`latex -output-directory={{pfad/zu/verzeichnis}} {{quelldatei.tex}}`

- Kompiliere ein DVI Dokument und stoppe bei jedem Fehler:

`latex -halt-on-error {{quelldatei.tex}}`
