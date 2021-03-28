# pdflatex

> Compile a PDF document from LaTeX source files.
> More information: <https://www.unix.com/man-page/redhat/1/pdflatex>.

- Compile a PDF document:

`pdflatex {{source.tex}}`

- Compile a PDF document specifying an output directory:

`pdflatex -output-directory={{path/to/directory}} {{source.tex}}`

- Compile a PDF document, halting on each error:

`pdflatex -halt-on-error {{source.tex}}`
