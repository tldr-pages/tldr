# brew

> Homebrew - gestore di pacchetti per macOS e Linux.
> Alcuni sottocomandi come `install` hanno la propria documentazione.
> Maggiori informazioni: <https://docs.brew.sh/Manpage>.

- Installa l'ultima versione stabile di una formula o cask:

`brew install {{formula|cask}}`

- Elenca tutte le formule e casks installate:

`brew list`

- Aggiorna una formula o cask installata (se non specificata, aggiorna tutto):

`brew upgrade {{formula|cask}}`

- Scarica l'ultima versione di Homebrew e di tutte le formule/casks dal repository:

`brew update`

- Mostra formule e casks con versioni più recenti disponibili:

`brew outdated`

- Cerca formule (pacchetti) e casks (pacchetti `.app` nativi macOS):

`brew search {{testo}}`

- Visualizza informazioni su una formula o cask (versione, percorso, dipendenze, etc.):

`brew info {{formula|cask}}`

- Controlla l'installazione locale di Homebrew per problemi:

`brew doctor`
