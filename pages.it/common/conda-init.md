# conda init

> Inizializza conda per l'interazione con la shell.
> La maggior parte delle shell deve essere chiusa e riaperta affinché le modifiche abbiano effetto.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/init.html>.

- Inizializza una shell specifica (se non specificata, predefinita `bash` su UNIX e `powershell` su Windows):

`conda init {{zsh|bash|powershell|fish|tcsh|xonsh}}`

- Inizializza tutte le shell disponibili:

`conda init --all`

- Inizializza conda per tutti gli utenti del sistema:

`conda init --system`

- Non inizializzare conda per l'utente corrente:

`conda init --no-user`

- Aggiungi la directory `condabin/` a `$PATH`:

`conda init --condabin`

- Annulla gli effetti dell'ultimo comando `conda init`:

`conda init --reverse`
