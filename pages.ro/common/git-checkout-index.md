# git checkout-index

> Copiați fișierele din index în arborele de lucru.
> Mai multe informaţii: <https://git-scm.com/docs/git-checkout-index>

- Restaurați orice fișiere șterse de la ultima comitere:

`git checkout-index --all`

- Restaurați orice fișiere șterse sau modificate de la ultima comitere:

`git checkout-index --all --force`

- Restaurați orice fișiere modificate de la ultima comitere, ignorând orice fișiere care au fost șterse:

`git checkout-index --all --force --no-create`

- Exportați o copie a întregului arbore la ultima angajare în directorul specificat (slash-ul final este important):

`git checkout-index --all --force --prefix={{path/to/export_directory/}}`
