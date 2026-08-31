# kpsewhich

> Standalone path lookup and variable expansion for the Kpathsea TeX library.
> More information: <https://manned.org/kpsewhich>.

- Locate a TeX or LaTeX file in the TeX directory structure:

`kpsewhich {{file_or_package.sty}}`

- Locate all matches for a specific file:

`kpsewhich --all {{file_or_package.sty}}`

- Locate a file with a specific format:

`kpsewhich --format={{tfm|bib|sty|cls|tex}} {{filename}}`

- Print the value of a specific TeX configuration variable:

`kpsewhich --var-value={{TEXMFDIST}}`

- Locate a file under a specific TeX engine context:

`kpsewhich --progname={{pdflatex}} {{filename}}`
