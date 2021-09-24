# brew bundle

> Bundler per Homebrew, Homebrew Cask e per il Mac App Store.
> Maggiori informazioni: <https://github.com/Homebrew/homebrew-bundle>.

- Installa un pacchetto da un Brewfile nel percorso corrente:

`brew bundle`

- Installa pacchetti da un Brewfile specifico in un percorso specifico:

`brew bundle --file={{percorso/del/file}}`

- Crea un Brewfile con tutti i pacchetti installati:

`brew bundle dump`

- Disinstalla tutti i pacchetti non specificati nel Brewfile:

`brew bundle cleanup --force`

- Controlla se c'è qualcosa da installare o da aggiornare nel Brewfile:

`brew bundle check`

- Mostra una lista di tutte le righe presenti nel Brewfile:

`brew bundle list --all`
