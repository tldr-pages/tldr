# po4a-updatepo

> Update the translation (in PO format) of a documentation.
> More information: <https://po4a.org/man/man1/po4a-updatepo.1.php>.

- Update a PO file according to the modification of its origin file:

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- List available formats:

`po4a-updatepo --help-format`

- Update several PO files according to the modification of their origin file:

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/po1.po}} --po {{path/to/po2.po}}`
