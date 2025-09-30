# texliveonfly

> Downloads missing TeX Live packages while compiling `.tex` files.
> More information: <https://ctan.org/tex-archive/support/texliveonfly>.

- Download missing packages while compiling:

`texliveonfly {{source.tex}}`

- Use a specific compiler (defaults to `pdflatex`):

`texliveonfly {{[-c|--compiler]}} {{compiler}} {{source.tex}}`

- Use a custom TeX Live `bin` folder:

`texliveonfly --texlive_bin={{path/to/texlive_bin}} {{source.tex}}`
