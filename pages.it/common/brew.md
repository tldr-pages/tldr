# brew

> Gestore di pacchetti per macOS.
> Maggiori informazioni: <https://docs.brew.sh/Manpage>.

- Installa l'ultima versione stabile di una formula (usa `--devel` per le versioni in sviluppo):

`brew install {{formula}}`

- Mostra tutte le formule installate:

`brew list`

- Aggiorna una formula installata (se non viene fornito il nome di nessuna formula, tutte le formule installate verranno aggiornate):

`brew upgrade {{formula}}`

- Trova la versione più aggiornata di Homebrew e di tutte le formule da GitHub:

`brew update`

- Cerca formule e cask:

`brew search {{testo}}`

- Mostra le informazioni su una specifica formula (versione, percorso di installazione, dipendenze, ecc...):

`brew info {{formula}}`

- Verifica se la versione installata di Homebrew presenta dei problemi:

`brew doctor`
