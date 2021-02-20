# texliveonfly

> Downloads missing TeX Live packages while compiling .tex files.
> More information: <https://ctan.org/pkg/texliveonfly>.

- Download missing packages while compiling:

`texliveonfly {{source.tex}}`

- Use specific compiler (defaults to pdflatex):

`texliveonfly --compiler={{compiler}} {{source.tex}}`

- Use specific TeX Live bin folder location:

`texliveonfly --texlive_bin={{/path/to/texlive_bin}} {{source.tex}}`
