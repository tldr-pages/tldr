# git annex

> Gestionați fișierele cu Git, fără a le verifica conținutul.
> Atunci când un fișier este anexat, conținutul său este mutat într-un magazin cheie valoare și se face un simlink care indică conținutul.
> Mai multe informaţii: <https://git-annex.branchable.com>

- Ajutor:

`git annex help`

- Inițializarea unui repo cu anexa Git:

`git annex init`

- Adaugă un fişier:

`git annex add {{path/to/file_or_directory}}`

- Afișează starea curentă a unui fișier sau a unui director:

`git annex status {{path/to/file_or_directory}}`

- Sincronizați un depozit local cu o telecomandă:

`git annex {{remote}}`

- Obțineți un fișier sau un director:

`git annex get {{path/to/file_or_directory}}`
