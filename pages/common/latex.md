# latex

> Compile a DVI document from LaTeX source files.
> More information: <https://linux.die.net/man/1/latex>.

- Compile a DVI document:

`latex {{source.tex}}`

- Compile a DVI document specifying an output directory:

`latex -output-directory={{path/to/directory}} {{source.tex}}`

- Compile a DVI document, halting on each error:

`latex -halt-on-error {{source.tex}}`
