# gpg-zip

> Criptați fișierele și directoarele dintr-o arhivă utilizând GPG.
> Mai multe informaţii: <https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>

- Criptați un director în `archive.gpg` folosind o frază de acces:

`gpg-zip --symmetric --output {{archive.gpg}} {{path/to/directory}}`

- Decriptează `archive.gpg` într-un director cu același nume:

`gpg-zip --decrypt {{path/to/archive.gpg}}`

- Listează conținutul „archive.gpg” criptat:

`gpg-zip --list-archive {{path/to/archive.gpg}}`
