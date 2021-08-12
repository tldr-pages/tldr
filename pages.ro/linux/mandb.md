# mandb

> Gestionați baza de date a paginilor manuale pre-formatate.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/mandb.8.html>

- Purjarea și procesarea paginilor manuale:

`mandb`

- Actualizaţi o singură intrare:

`mandb --filename {{path/to/file}}`

- Creați intrări de la zero în loc să actualizați:

`mandb --create`

- Doar procesați bazele de date ale utilizatorilor:

`mandb --user-db`

- Nu purjați intrările depășite:

`mandb --no-purge`

- Verificați validitatea paginilor manuale:

`mandb --test`
