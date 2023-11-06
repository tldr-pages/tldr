# brew cask

> Gestore di pacchetti per applicazioni macOS distribuite sotto forma di file binari.
> Maggiori informazioni: <https://github.com/Homebrew/homebrew-cask>.

- Cerca formule e cask:

`brew search {{testo}}`

- Installa un cask:

`brew cask install {{nome_del_cask}}`

- Elenca tutti i cask installati:

`brew cask list`

- Elenca i cask installati con versioni più nuove disponibili:

`brew cask outdated`

- Aggiorna un cask installato (se non viene fornito il nome di nessun cask, tutti i cask saranno aggiornati):

`brew cask upgrade {{nome_del_cask}}`

- Disinstalla un cask:

`brew cask uninstall {{nome_del_cask}}`

- Disinstalla un cask e rimuovi i relativi file e impostazioni:

`brew cask zap {{nome_del_cask}}`

- Mostra informazioni su uno specifico cask:

`brew cask info {{nome_del_cask}}`
