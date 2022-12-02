# tex

> Compile a DVI document from TeX source files.
> More information: <https://www.tug.org/begin.html>.

- Compile a DVI document:

`tex {{path/to/source.tex}}`

- Compile a DVI document, specifying an output directory:

`tex -output-directory={{path/to/directory}} {{path/to/source.tex}}`

- Compile a DVI document, exiting on each error:

`tex -halt-on-error {{path/to/source.tex}}`
