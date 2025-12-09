# latexmk

> Compile LaTeX source files into finished documents.
> Automatically does multiple runs when needed.
> More information: <https://mg.readthedocs.io/latexmk.html>.

- Compile a DVI (Device Independent file) document from every source:

`latexmk`

- Compile a DVI document from a specific source file:

`latexmk {{path/to/source.tex}}`

- Compile a PDF document:

`latexmk -pdf {{path/to/source.tex}}`

- Open the document in a viewer and continuously update it whenever source files change:

`latexmk -pvc {{path/to/source.tex}}`

- Force the generation of a document even if there are errors:

`latexmk -f {{path/to/source.tex}}`

- Clean up temporary TEX files created for a specific TEX file:

`latexmk -c {{path/to/source.tex}}`

- Clean up all temporary TEX files in the current directory:

`latexmk -c`
