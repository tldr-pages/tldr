# git commit-tree

> Utilitar de nivel scăzut pentru a crea obiecte comite.
> A se vedea de asemenea: `git comitet”.
> Mai multe informaţii: <https://git-scm.com/docs/git-commit-tree>

- Creați un obiect comite cu mesajul specificat:

`git commit-tree {{tree}} -m "{{message}}"`

- Creați un obiect de comitere care citește mesajul dintr-un fișier (utilizați `-` pentru stdin):

`git commit-tree {{tree}} -F {{path/to/file}}`

- Crearea unui obiect de comite semnat GPG:

`git commit-tree {{tree}} -m "{{message}}" --gpg-sign`

- Creați un obiect de comitere cu obiectul de comitere părinte specificat:

`git commit-tree {{tree}} -m "{{message}}" -p {{parent_commit_sha}}`
