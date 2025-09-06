# tex

> Kompiliere eine TeX Quelldatei in ein DVI Dokument.
> Weitere Informationen: <https://www.tug.org/begin.html>.

- Kompiliere ein DVI Dokument:

`tex {{quelldatei.tex}}`

- Kompiliere ein DVI Dokument und gib ein bestimmtes Output-Verzeichnis an:

`tex -output-directory={{pfad/zu/verzeichnis}} {{quelldatei.tex}}`

- Kompiliere ein DVI Dokument und stoppe bei jedem Fehler:

`tex -halt-on-error {{quelldatei.tex}}`
