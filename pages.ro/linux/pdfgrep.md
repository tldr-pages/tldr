# pdfgrep

> Căutare text în fişiere PDF.

- Găsiți linii care se potrivesc modelului într-un PDF:

`pdfgrep {{pattern}} {{file.pdf}}`

- Includeți numele fișierului și numărul paginii pentru fiecare linie potrivită:

`pdfgrep --with-filename --page-number {{pattern}} {{file.pdf}}`

- Faceți o căutare insensibilă la caz pentru linii care încep cu „foo” și returnați primele 3 meciuri:

`pdfgrep --max-count {{3}} --ignore-case {{'^foo'}} {{file.pdf}}`

- Găsiți tipar în fișierele cu o extensie `.pdf` în directorul curent recursiv:

`pdfgrep --recursive {{pattern}}`

- Găsiți model pe fișiere care se potrivesc cu un anumit glob în directorul curent recursiv:

`pdfgrep --recursive --include {{'*book.pdf'}} {{pattern}}`
