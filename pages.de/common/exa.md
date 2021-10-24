# exa

> Ein moderner Ersatz für `ls` (Verzeichnisinhalte auflisten).
> Weitere Informationen: <https://the.exa.website>.

- Liste eine Datei pro Zeile auf:

`exa --oneline`

- Liste alle Dateien auf, einschließlich versteckter Dateien:

`exa --all`

- Liste alle Dateien im langen Format auf (Berechtigungen, Eigentümer, Größe und Änderungsdatum):

`exa --long --all`

- Liste Dateien nach Größe absteigend sortiert auf:

`exa --reverse --sort={{size}}`

- Zeige Dateien in einer Baumstruktur an, die drei Ebenen tief ist:

`exa --long --tree --level={{3}}`

- Liste Dateien nach Änderungsdatum aufsteigend sortiert auf:

`exa --long --sort={{modified}}`

- Liste Dateien inklusive Header, Icons und Git-Status:

`exa --long --header --icons --git`

- Liste keine Dateien auf, die in `.gitignore` erwähnt werden:

`exa --git-ignore`
