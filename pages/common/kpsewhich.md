# kpsewhich

> Find TeX-related files and expand Kpathsea variables and paths.
> More information: <https://manned.org/kpsewhich>.

- Find a file in the TeX search path:

`kpsewhich {{article.cls}}`

- Find a file using a specific file format:

`kpsewhich -format {{tex}} {{plain.tex}}`

- Show the search path for a specific file format:

`kpsewhich -show-path {{tex}}`

- Print the value of a Kpathsea variable:

`kpsewhich -var-value {{TEXMFHOME}}`

- Search for a file in a specific path:

`kpsewhich -path {{path/to/directory}} {{filename}}`
