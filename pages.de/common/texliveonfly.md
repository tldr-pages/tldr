# texliveonfly

> Lade fehlende TeX Live Packages während dem Kompilieren einer `.tex` Datei herunter.
> Weitere Informationen: <https://ctan.org/pkg/texliveonfly>.

- Lade fehlende Packages während dem Kompilieren herunter:

`texliveonfly {{quelldatei.tex}}`

- Verwende einen bestimmten Compiler (standardmäßig `pdflatex`):

`texliveonfly --compiler={{compiler}} {{quelldatei.tex}}`

- Verwende ein bestimmtes Tex Live `bin` Verzeichnis:

`texliveonfly --texlive_bin={{pfad/zu/texlive_bin}} {{quelldatei.tex}}`
