# qpdf

> Software versatil de transformare PDF.
> Mai multe informaţii: <https://github.com/qpdf/qpdf>

- Extrageţi paginile 1-3, 5 şi 6-10 dintr-un fişier PDF şi salvaţi-le ca altul:

`qpdf --empty --pages {{input.pdf}} {{1-3,5,6-10}} -- {{output.pdf}}`

- Mergeți (concatenați) toate paginile unei liste de fișiere PDF și salvați rezultatul ca PDF nou:

`qpdf --empty --pages {{file1.pdf}} {{file2.pdf}} {{file3.pdf}} -- {{output.pdf}}`

- Mergeți (concatenați) paginile date dintr-o listă de fișiere PDF și salvați rezultatul ca PDF nou:

`qpdf --empty --pages {{file1.pdf}} {{1,6-8}} {{file2.pdf}} {{3,4,5}} -- {{output.pdf}}`

- Scrieți fiecare grup de n pagini într-un fișier de ieșire separat cu un model de nume de fișier dat:

`qpdf --split-pages=n {{input.pdf}} {{out_%d.pdf}}`

- Rotiți anumite pagini ale unui pdf cu un unghi dat:

`qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{input.pdf}} {{output.pdf}}`

- Eliminați parola dintr-un fișier protejat prin parolă:

`qpdf --password={{password}} --decrypt {{input.pdf}} {{output.pdf}}`
