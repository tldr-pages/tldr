# kpsewhich

> Standalone path lookup and expansion for the TeX Kpathsea library.
> More information: <https://manned.org/kpsewhich>.

- Locate a LaTeX style or class file:

`kpsewhich {{article.cls}}`

- Look up a file for a specific format:

`kpsewhich -format={{bib|tex|tfm|map}} {{filename}}`

- List all occurrences of a file across search paths:

`kpsewhich -all {{filename}}`

- Print the value of a TeX configuration variable:

`kpsewhich -var-value={{TEXMFHOME|TEXMFDIST|TEXINPUTS}}`

- Search along a specific path instead of the default search path:

`kpsewhich -path={{path/to/directory}} {{filename}}`

- Specify the target TeX engine for format-specific lookups:

`kpsewhich -engine={{pdftex|luatex|xetex}} {{filename}}`

- Display help:

`kpsewhich --help`
