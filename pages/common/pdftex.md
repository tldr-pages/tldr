# pdftex

> Compile a PDF document from TeX source files.
> More information: <https://www.tug.org/applications/pdftex/>.

- Compile a PDF document:

`pdftex {{path/to/source.tex}}`

- Compile a PDF document, specifying an output directory:

`pdftex -output-directory={{path/to/directory}} {{path/to/source.tex}}`

- Compile a PDF document, exiting on each error:

`pdftex -halt-on-error {{path/to/source.tex}}`
