# zip2john

> A jelszóhash-ok kivonására szolgáló eszköz a zip-fájlokból a John the Ripper jelszófeltörővel való használatra. Ez egy segédeszköz, amelyet általában a John the Ripper telepítésének részeként telepítenek. További információ: <https://www.openwall.com/john/>.

- Kivonatolja a jelszóhash-t egy archívumból, felsorolva az összes fájlt az archívumban:

`zip2john {{path/to/file.zip}}`

- A jelszó hash kivonatolása \[o\]nly egy adott tömörített fájl segítségével:

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}}`

- A jelszó hash kivonatolása egy tömörített fájlból egy adott fájlba (John the Ripperrel való használatra):

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}} > {{file.hash}}`
