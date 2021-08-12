# pandoc

> Conversia documentelor între diferite formate.
> Mai multe informaţii: <https://pandoc.org>

- Conversia fișierului în pdf (formatul de ieșire este determinat de extensia fișierului):

`pandoc {{input.md}} -o {{output.pdf}}`

- Forțați conversia pentru a utiliza un anumit format:

`pandoc {{input.docx}} --to {{gfm}} -o {{output.md}}`

- Conversia într-un fișier independent cu antetele/subsolurile corespunzătoare (pentru LaTeX, HTML etc.):

`pandoc {{input.md}} -s -o {{output.tex}}`

- Listează toate formatele de intrare acceptate:

`pandoc --list-input-formats`

- Listează toate formatele de ieșire acceptate:

`pandoc --list-output-formats`
