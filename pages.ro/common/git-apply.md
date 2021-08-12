# git apply

> Aplicați o corecție fișierelor și/sau indexului.
> Mai multe informaţii: <https://git-scm.com/docs/git-apply>

- Imprimați mesaje despre fișierele patch-uri:

`git apply --verbose {{path/to/file}}`

- Aplicați și adăugați fișierele patch-uri la index:

`git apply --index {{path/to/file}}`

- Aplicați un fișier de corecție la distanță:

`curl {{https://example.com/file.patch}} | git apply`

- Difstat de ieșire pentru intrare și se aplică plasturele:

`git apply --stat --apply {{path/to/file}}`

- Aplicaţi plasturele în sens invers:

`git apply --reverse {{path/to/file}}`

- Stocaţi rezultatul plasturelui în index fără a modifica arborele de lucru:

`git apply --cache {{path/to/file}}`
