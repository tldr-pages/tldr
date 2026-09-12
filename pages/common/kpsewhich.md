# kpsewhich

> Find TeX-related files and expand Kpathsea variables and paths.
> See also: `tex`, `latex`, `mktexfmt`.
> More information: <https://manned.org/kpsewhich>.

- Find a file in the TeX search path (format inferred from the extension):

`kpsewhich {{article.cls}}`

- Find a file using a specific file format:

`kpsewhich -format {{tex}} {{plain.tex}}`

- Show the search path for a specific file format:

`kpsewhich -show-path {{tex}}`

- Print the expanded value of a Kpathsea variable:

`kpsewhich -var-value {{TEXMFHOME}}`

- Expand variables in a string:

`kpsewhich -expand-var '{{$TEXMFDIST/tex}}'`

- Search for a file only in a specific path:

`kpsewhich -path {{path/to/directory}} {{filename}}`
