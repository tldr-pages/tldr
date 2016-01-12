# latexmk

> Compile LaTeX source files into finished documents.
> Automatically does multiple runs when needed.

- Compile a dvi (DeVice Independent file) document from every source:

`latexmk`

- Compile a dvi document from a specific source file:

`latexmk {{source.tex}}`

- Compile a pdf document:

`latexmk -pdf {{source.tex}}`

- Clean up all temporary tex files in the folder:

`latexmk -c`

- Clean up temporary tex files created for a specific tex file:

`latexmk -c {{source.tex}}`

- Clean up temporary tex and output files:

`latexmk -C`
