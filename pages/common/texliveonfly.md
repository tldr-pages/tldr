# texliveonfly

> Downloads missing TeX Live packages while compiling `.tex` files.
> More information: <https://ctan.org/pkg/texliveonfly>.

- Download missing packages while compiling:

`texliveonfly {{path/to/source.tex}}`

- Use a specific compiler (defaults to `pdflatex`):

`texliveonfly --compiler={{compiler}} {{path/to/source.tex}}`

- Use a custom TeX Live `bin` folder:

`texliveonfly --texlive_bin={{path/to/texlive_bin}} {{path/to/source.tex}}`
