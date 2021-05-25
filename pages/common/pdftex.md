# pdftex

> Compile a PDF document from TeX source files.
> More information: <https://www.tug.org/applications/pdftex/>.

- Compile a PDF document:

`pdftex {{source.tex}}`

- Compile a PDF document, specifying an output directory:

`pdftex -output-directory={{path/to/directory}} {{source.tex}}`

- Compile a PDF document, halting on each error:

`pdftex -halt-on-error {{source.tex}}`
