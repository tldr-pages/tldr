# pdflatex

> Compile a PDF document from LaTeX source files.

- Compile a PDF document:

`pdflatex {{source.tex}}`

- Compile a PDF document specifying an output directory:

`pdflatex -output-directory={{path/to/directory}} {{source.tex}}`

- Compile a PDF document, halting on each error:

`pdflatex -halt-on-error {{source.tex}}`
