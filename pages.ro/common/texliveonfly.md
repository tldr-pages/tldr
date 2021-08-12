# texliveonfly

> Descărcări lipsă de pachete teX Live în timpul compilării fişierelor `.tex'.
> Mai multe informaţii: <https://ctan.org/pkg/texliveonfly>

- Descărcați pachetele lipsă în timpul compilării:

`texliveonfly {{source.tex}}`

- Utilizați un compilator specific (implicit la `pdflatex`):

`texliveonfly --compiler={{compiler}} {{source.tex}}`

- Folosește un folder personalizat Tex Live `bin`:

`texliveonfly --texlive_bin={{path/to/texlive_bin}} {{source.tex}}`
