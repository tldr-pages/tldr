# fortune

> Print a random quotation (fortune-cookie style).
> More information: <https://manned.org/fortune>.

- Print a quotation:

`fortune`

- Print an [o]ffensive quotation:

`fortune -o`

- Print a [l]ong quotation:

`fortune -l`

- Print a [s]hort quotation:

`fortune -s`

- List the available quotation database [f]iles:

`fortune -f`

- Print a quotation from one of the database files listed by `fortune -f`:

`fortune {{path/to/file}}`

- Pipe a fortune through another command (like `cowsay` or `lolcat`):

`fortune | cowsay | lolcat`
