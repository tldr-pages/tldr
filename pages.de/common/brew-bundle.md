# brew bundle

> Bundler für Homebrew, Homebrew Cask und den Mac App Store.
> Weitere Informationen: <https://github.com/Homebrew/homebrew-bundle>.

- Installiere Pakete aus einer Brewfile im aktuellen Pfad:

`brew bundle`

- Installiere Pakete aus einer bestimmten Brewfile:

`brew bundle --file {{pfad/zu/brewfile}}`

- Gib eine Liste mit allen installierten Paketen aus:

`brew bundle dump`

- Deinstalliere Pakete, die nicht in der Brewfile aufgelistet sind:

`brew bundle cleanup --force`

- Prüfe, ob von einem Paket die aktuellste Version installiert ist:

`brew bundle check`

- Zeige alle Pakete, die in der Brewfile aufgelistet sind:

`brew bundle list --all`
