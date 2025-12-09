# xetex

> Compile a PDF document from XeTeX source files.
> More information: <https://www.tug.org/xetex/>.

- Compile a PDF document:

`xetex {{source.tex}}`

- Compile a PDF document, specifying an output directory:

`xetex -output-directory={{path/to/directory}} {{source.tex}}`

- Compile a PDF document, exiting if errors occur:

`xetex -halt-on-error {{source.tex}}`
