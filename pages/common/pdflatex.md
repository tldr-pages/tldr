# pdflatex

> Compile a PDF document from LaTeX source files.
> More information: <https://manned.org/pdflatex>.

- Compile a PDF document:

`pdflatex {{path/to/source.tex}}`

- Compile a PDF document specifying an output directory:

`pdflatex -output-directory={{path/to/directory}} {{path/to/source.tex}}`

- Compile a PDF document, exiting on each error:

`pdflatex -halt-on-error {{path/to/source.tex}}`
