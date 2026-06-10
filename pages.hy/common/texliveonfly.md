# texliveonfly

> Ներբեռնում է բացակայող TeX Live փաթեթները `.tex` ֆայլեր կազմելիս:.
> Լրացուցիչ տեղեկություններ. <https://ctan.org/tex-archive/support/texliveonfly>:.

- Ներբեռնեք բացակայող փաթեթները կազմելիս.:

`texliveonfly {{source.tex}}`

- Օգտագործեք հատուկ կոմպիլյատոր (կանխադրված է `pdflatex`):

`texliveonfly {{[-c|--compiler]}} {{compiler}} {{source.tex}}`

- Օգտագործեք հատուկ TeX Live `bin` թղթապանակ.:

`texliveonfly --texlive_bin={{path/to/texlive_bin}} {{source.tex}}`
