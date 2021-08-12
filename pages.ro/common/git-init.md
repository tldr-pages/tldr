# git init

> Inițializează un nou depozit local Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-init>

- Iniţializează un nou depozit local:

`git init`

- Inițializarea unui depozit cu numele specificat pentru sucursala inițială:

`git init --initial-branch={{branch_name}}`

- Inițializați un depozit utilizând SHA256 pentru hash-uri de obiecte (necesită versiunea Git 2.29+):

`git init --object-format={{sha256}}`

- Inițializarea unui depozit gol, potrivit pentru utilizare ca telecomandă peste ssh:

`git init --bare`
