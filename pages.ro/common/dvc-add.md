# dvc add

> Adăugați fișiere modificate la index.
> Mai multe informaţii: <https://dvc.org/doc/command-reference/add>

- Adăugați un fișier țintă unic la index:

`dvc add {{path/to/file}}`

- Adăugați un director țintă la index:

`dvc add {{path/to/directory}}`

- Adaugă recursiv toate fișierele într-un director țintă dat:

`dvc add --recursive {{path/to/directory}}`

- Adaugă un fișier țintă cu un nume de fișier personalizat `.dvc`:

`dvc add --file {{custom_name.dvc}} {{path/to/file}}`
