# pdftk

> Setul de instrumente PDF.
> Mai multe informaţii: <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>

- Extrageţi paginile 1-3, 5 şi 6-10 dintr-un fişier PDF şi salvaţi-le ca altul:

`pdftk {{input.pdf}} cat {{1-3 5 6-10}} output {{output.pdf}}`

- Mergeți (concatenați) o listă de fișiere PDF și salvați rezultatul ca altul:

`pdftk {{file1.pdf file2.pdf ...}} cat output {{output.pdf}}`

- Împărțiți fiecare pagină a unui fișier PDF într-un fișier separat, cu un anumit model de ieșire de nume de fișier:

`pdftk {{input.pdf}} burst output {{out_%d.pdf}}`

- Rotiți toate paginile cu 180 de grade în sensul acelor de ceasornic:

`pdftk {{input.pdf}} cat {{1-endsouth}} output {{output.pdf}}`

- Rotiți a treia pagină cu 90 de grade în sensul acelor de ceasornic și lăsați altele neschimbate:

`pdftk {{input.pdf}} cat {{1-2 3east 4-end}} output {{output.pdf}}`
