# pdftex

> Kompiliere eine TeX Quelldatei in ein PDF Dokument.
> Mehr Informationen: <https://www.tug.org/applications/pdftex/>.

- Kompiliere ein PDF Dokument:

`pdftex {{quelldatei.tex}}`

- Kompiliere ein PDF Dokument und gib ein bestimmtes Output-Verzeichnis an:

`pdftex -output-directory={{pfad/zu/verzeichnis}} {{quelldatei.tex}}`

- Kompiliere ein PDF Dokument und stoppe bei jedem Fehler:

`pdftex -halt-on-error {{quelldatei.tex}}`
