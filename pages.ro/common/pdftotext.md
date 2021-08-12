# pdftotext

> Conversia fișierelor PDF în format text simplu.

- Convertiți `fișier.pdf` în text simplu și imprimați-l la ieșire standard:

`pdftotext {{filename.pdf}} -`

- Convertiți `fișier.pdf` în text simplu și salvați-l ca `nume de fișier.txt`:

`pdftotext {{filename.pdf}}`

- Convertiți `fișier.pdf` în text simplu și păstrați aspectul:

`pdftotext -layout {{filename.pdf}}`

- Conversia `input.pdf` in text simplu si salvati-l ca `output.txt`:

`pdftotext {{input.pdf}} {{output.txt}}`

- Convertiți paginile 2, 3 și 4 din `input.pdf` în text simplu și salvați-le ca „output.txt`:

`pdftotext -f {{2}} -l {{4}} {{input.pdf}} {{output.txt}}`
