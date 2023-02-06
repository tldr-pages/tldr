# gnucash-cli

> A GnuCash parancssori változata. További információ: <https://gnucash.org>.

- Egy fájlban megadott valuták és részvények árfolyamainak lekérése és kinyomtatása:

`gnucash-cli --quotes get {{path/to/file.gnucash}}`

- A `--name` által meghatározott típusú pénzügyi jelentés generálása:

`gnucash-cli --report run --name "{{Balance Sheet}}" {{path/to/file.gnucash}}`
