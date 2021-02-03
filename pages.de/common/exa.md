# exa

> Ein moderner Ersatz für `ls` (Verzeichnisinhalte auflisten).
> Mehr Informationen: <https://the.exa.website>.

- Listet pro Zeile eine Datei auf:

`exa --oneline`

- Alle Dateien auflisten, einschließlich versteckter Dateien:

`exa --all`

- Lange Formatliste (Berechtigungen, Eigentümer, Größe und Änderungsdatum) aller Dateien:

`exa --long --all`

- Listen Sie die Dateien mit den größten oben auf:

`exa --reverse --sort={{size}}`

- Zeigt Dateien in einer Baumstruktur an, der drei Ebenen tief ist:

`exa --long --tree --level={{3}}`

- Dateien nach Änderungsdatum sortiert auflisten (älteste zuerst):

`exa --long --sort={{modified}}`
