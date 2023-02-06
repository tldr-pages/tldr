# diff-pdf

> Eszköz két PDF összehasonlítására. További információ: <https://github.com/vslavik/diff-pdf>.

- PDF-ek összehasonlítása, a változások jelzése visszatérési kódokkal (`0` = nincs különbség, `1` = a PDF-ek különböznek):

`diff-pdf {{path/to/a.pdf}} {{path/to/b.pdf}}`

- PDF-ek összehasonlítása, PDF-kimenet a vizuálisan kiemelt különbségekkel:

`diff-pdf --output-diff={{path/to/diff.pdf}} {{path/to/a.pdf}} {{path/to/b.pdf}}`

- PDF-ek összehasonlítása, a különbségek megtekintése egy egyszerű grafikus felületen:

`diff-pdf --view {{path/to/a.pdf}} {{path/to/b.pdf}}`
