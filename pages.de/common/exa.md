# exa

> Ein moderner Ersatz für `ls` (Verzeichnisinhalte auflisten).
> Weitere Informationen: <https://github.com/ogham/exa#command-line-options>.

- Liste eine Datei pro Zeile auf:

`exa {{[-1|--oneline]}}`

- Liste alle Dateien auf, einschließlich versteckter Dateien:

`exa {{[-a|--all]}}`

- Liste alle Dateien im langen Format auf (Berechtigungen, Eigentümer, Größe und Änderungsdatum):

`exa {{[-l|--long]}} {{[-a|--all]}}`

- Liste Dateien nach Größe absteigend sortiert auf:

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Zeige Dateien in einer Baumstruktur an, die drei Ebenen tief ist:

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- Liste Dateien nach Änderungsdatum aufsteigend sortiert auf:

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Liste Dateien inklusive Header, Icons und Git-Status:

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- Liste keine Dateien auf, die in `.gitignore` erwähnt werden:

`exa --git-ignore`
