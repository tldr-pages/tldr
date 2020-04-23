# pdflatex

> Compile a pdf document from LaTeX source files.

- Compile a pdf document:

`pdflatex {{source.tex}}`

- Compile a pdf document specifying an output directory:

`pdflatex -output-directory={{path/to/directory}} {{source.tex}}`

- Compile a pdf document, halting on each error:

`pdflatex -halt-on-error {{source.tex}}`
