# daps

> A DAPS egy nyílt forráskódú program a DocBook XML átalakítására olyan kimeneti formátumokba, mint a HTML vagy a PDF. További információ: <https://opensuse.github.io/daps/doc/index.html>.

- Ellenőrizze, hogy egy DocBook XML fájl érvényes-e:

`daps -d {{path/to/file.xml}} validate`

- DocBook XML fájl átalakítása PDF-be:

`daps -d {{path/to/file.xml}} pdf`

- Egy DocBook XML fájl átalakítása egyetlen HTML-fájllá:

`daps -d {{path/to/file.xml}} html --single`

- Súgó megjelenítése:

`daps --help`

- Verzió megjelenítése:

`daps --version`
