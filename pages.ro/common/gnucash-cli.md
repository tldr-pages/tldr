# gnucash-cli

> O versiune în linia Către de comandă a GnuCash.
> Mai multe informaţii: <https://gnucash.org>

- Obțineți cotații pentru valute și stocuri specificate într-un fișier și imprimați-le:

`gnucash-cli --quotes get {{path/to/file.gnucash}}`

- Generează un raport financiar de un anumit tip, specificat după `—nume`:

`gnucash-cli --report run --name "{{Balance Sheet}}" {{path/to/file.gnucash}}`
