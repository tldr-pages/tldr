# latexpand

> Simplify LaTeX source files by removing comments and resolving `\include`s, `\input`s, etc.
> More information: <https://www.ctan.org/pkg/latexpand>.

- Simplify the specified source file and save the result to the specified output file:

`latexpand {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Do not remove comments:

`latexpand --keep-comments {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Do not expand `\include`s, `\input`s etc.:

`latexpand --keep-includes {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Expand `\usepackage`s as far as the corresponding STY files can be found:

`latexpand --expand-usepackage {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- Inline the specified BBL file:

`latexpand --expand-bbl {{path/to/bibliography.bbl}} {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`
