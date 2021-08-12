# rector

> Un instrument automat pentru actualizarea și refactorizarea codului PHP 5.3+.
> Mai multe informaţii: <https://github.com/rectorphp/rector>

- Procesați un anumit director:

`rector process {{path/to/directory}}`

- Procesați un director fără a aplica modificări (rulare uscată):

`rector process {{path/to/directory}} --dry-run`

- Procesați un director și aplicați standarde de codificare:

`rector process {{path/to/directory}} --with-style`

- Afișează o listă a nivelurilor disponibile:

`rector levels`

- Procesați un director cu un anumit nivel:

`rector process {{path/to/directory}} --level {{level_name}}`
