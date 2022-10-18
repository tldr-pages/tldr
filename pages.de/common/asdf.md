# asdf

> Verwalte installierte Versionen von verschiedenen Paketen.
> Plugins (z.B. asdf-node) werden für spezifische Pakete verwendet.
> Weitere Informationen: <https://asdf-vm.com>.

- Liste alle verfügbaren Plugins auf:

`asdf plugin list all`

- Installiere ein neues Plugin:

`asdf plugin add {{name}}`

- Liste alle verfügbaren Versionen für ein Paket auf:

`asdf list all {{name}}`

- Installiere eine spezifische Version eines Pakets:

`asdf install {{name}} {{version}}`

- Lege die globale Version für ein Paket fest:

`asdf global {{name}} {{version}}`

- Lege die lokale Version für ein Paket fest:

`asdf local {{name}} {{version}}`
