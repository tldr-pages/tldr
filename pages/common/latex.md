# latex

> Compile a DVI document from LaTeX source files.
> More information: <https://texdoc.org/serve/tex.man1.pdf/0>.

- Compile a DVI document:

`latex {{source.tex}}`

- Compile a DVI document, specifying an output directory:

`latex -output-directory={{path/to/directory}} {{source.tex}}`

- Compile a DVI document, exiting on each error:

`latex -halt-on-error {{source.tex}}`
