# mutool

> Conversia fișierelor PDF, interogarea informațiilor și extragerea datelor.
> Mai multe informaţii: <https://mupdf.com/docs>

- Conversia paginilor 1-10 în 10 imagini PNG:

`mutool convert -o {{image%d.png}} {{file.pdf}} {{1-10}}`

- Conversia paginilor 2, 3 și 5 ale unui PDF în text în ieșirea standard:

`mutool draw -F {{txt}} {{file.pdf}} {{2,3,5}}`

- Concatenează două PDF-uri:

`mutool merge -o {{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- Interogare informaţii despre tot conţinutul încorporat într-un PDF:

`mutool info {{input.pdf}}`

- Extrageţi toate imaginile, fonturile şi resursele încorporate într-un PDF în directorul curent:

`mutool extract {{input.pdf}}`

- Imprimați conturul (cuprins) unui PDF:

`mutool show {{input.pdf}} outline`
