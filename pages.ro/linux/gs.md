# gs

> GhostScript este un interpret PDF și PostScript.
> Mai multe informaţii: <https://manned.org/gs>

- Pentru a vizualiza un fișier:

`gs -dQUIET -dBATCH {{file.pdf}}`

- Reduceți dimensiunea fișierului PDF la 150 dpi imagini pentru citirea pe un dispozitiv de carte electronică:

`gs -dNOPAUSE -dQUIET -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile={{output.pdf}} {{input.pdf}}`

- Conversia fişierului PDF (paginile 1 până la 3) într-o imagine cu o rezoluţie de 150 dpi:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -dFirstPage={{1}} -dLastPage={{3}} -sOutputFile={{output_%d.jpg}} {{input.pdf}}`

- Extragerea paginilor dintr-un fișier PDF:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.pdf}}`

- Îmbinarea fişierelor PDF:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- Conversia din fişierul PostScript în fişier PDF:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.ps}}`
