# xmllint

> XML elemző és linter, amely támogatja az XPath-ot, az XML fák navigálására szolgáló szintaxist. További információ: <https://manned.org/xmllint>.

- A "foo" nevű összes csomópont (tag) visszaadása:

`xmllint --xpath "//{{foo}}" {{source_file.xml}}`

- A "foo" nevű első csomópont tartalmának stringként történő visszaadása:

`xmllint --xpath "string(//{{foo}})" {{source_file.xml}}`

- A második horgonyzó elem href attribútumának visszaadása egy HTML-fájlban:

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- Ember által olvasható (behúzott) XML visszaadása a fájlból:

`xmllint --format {{source_file.xml}}`

- Annak ellenőrzése, hogy egy XML-fájl megfelel-e a DOCTYPE-nyilatkozatban foglalt követelményeknek:

`xmllint --valid {{source_file.xml}}`

- Az XML validálása az online tárolt DTD-séma alapján:

`xmllint --dtdvalid {{URL}} {{source_file.xml}}`
