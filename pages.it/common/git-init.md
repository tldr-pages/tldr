# git init

> Inizializza un nuovo repository Git locale.
> Maggiori informazioni: <https://git-scm.com/docs/git-init>.

- Inizializza un nuovo repository locale:

`git init`

- Inizializza un repository con il nome specificato per il ramo iniziale:

`git init --initial-branch={{nome_ramo}}`

- Inizializza un repository usando SHA256 per gli hash degli oggetti (richiede Git versione 2.29+):

`git init --object-format={{sha256}}`

- Inizializza un repository di soli dati, adatto per essere usato come server remoto accessibile via ssh:

`git init --bare`
