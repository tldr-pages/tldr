# brew install

> Installa una formula o un cask Homebrew.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- Installa una formula/cask:

`brew install {{formula|cask}}`

- Compila e installa una formula da sorgente (le dipendenze verranno comunque installate dai bottle):

`brew install {{[-s|--build-from-source]}} {{formula}}`

- Scarica il manifesto, mostra cosa verrebbe installato ma non installare nulla:

`brew install {{[-n|--dry-run]}} {{formula|cask}}`
