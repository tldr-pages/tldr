# git mv

> Mutați sau redenumiți fișiere și actualizați indexul Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-mv>

- Mutați fișierul în interiorul repo și adăugați mișcarea la următoarea comite:

`git mv {{path/to/file}} {{new/path/to/file}}`

- Redenumiți fișierul și adăugați redenumire la următoarea comitere:

`git mv {{filename}} {{new_filename}}`

- Suprascrie fișierul în calea țintă dacă există:

`git mv --force {{file}} {{target}}`
