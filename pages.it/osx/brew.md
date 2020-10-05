# brew

> Gestore di pacchetti per macOS.
> Più informazioni: <https://brew.sh>.

- Cerca formule e cask:

`brew search {{testo}}`

- Installa l'ultima versione stabile di una formula (usa `--devel` per le versioni in sviluppo):

`brew install {{formula}}`

- Mostra tutte le formule installate:

`brew list`

- Mostra le formule installate che non sono dipendenze di un'altra formula installata:

`brew leaves`

- Aggiorna una formula installata (se non viene fornito il nome di nessuna formula, tutte le formule installate verranno aggiornate):

`brew upgrade {{formula}}`

- Trova la versione più aggiornata di Homebrew e di tutte le formule da Github: 

`brew update`

- Rimuovi le vecchie versioni di una specifica formula installata (se nessuna formula viene specificata, tutte le formule saranno processate):

`brew cleanup {{formula}}`

- Mostra le informazioni su una specifica formula (versione, percorso di installazione, dipendenze, ecc...):

`brew info {{formula}}`

- Verifica se la versione installata di Homebrew presenta dei problemi:

`brew doctor`
