# qpdf

> Sokoldalú PDF átalakító szoftver. További információ: <https://github.com/qpdf/qpdf>.

- Kivonja az 1-3., 5. és 6-10. oldalt egy PDF-fájlból, és elmenti egy másik PDF-fájlba:

`qpdf --empty --pages {{input.pdf}} {{1-3,5,6-10}} -- {{output.pdf}}`

- Egy PDF-fájlok listájának összes oldalának egyesítése (összefűzése) és az eredmény új PDF-ként történő mentése:

`qpdf --empty --pages {{file1.pdf}} {{file2.pdf}} {{file3.pdf}} -- {{output.pdf}}`

- PDF-fájlok listájának adott oldalainak összevonása (egybekapcsolása) és az eredmény új PDF-ként történő mentése:

`qpdf --empty --pages {{file1.pdf}} {{1,6-8}} {{file2.pdf}} {{3,4,5}} -- {{output.pdf}}`

- Minden egyes n oldalból álló csoport írása egy különálló kimeneti fájlba egy adott fájlnévmintával:

`qpdf --split-pages=n {{input.pdf}} {{out_%d.pdf}}`

- A PDF egyes oldalainak adott szögben történő elforgatása:

`qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{input.pdf}} {{output.pdf}}`

- Jelszó eltávolítása egy jelszóval védett fájlból:

`qpdf --password={{password}} --decrypt {{input.pdf}} {{output.pdf}}`
