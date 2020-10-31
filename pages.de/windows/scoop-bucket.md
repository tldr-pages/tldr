# scoop bucket

> Verwalte "Eimer": Git-Repositories, welche Dateien enthalten, die beschreiben, wie Scoop Programme installiert.
> Kennt Scoop nicht die URL eines Eimers, so muss diese angegeben werden.
> Mehr Informationen: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Liste alle Eimer auf, die gerade aktiv sind:

`scoop bucket list`

- Liste alle bekannten Eimer auf:

`scoop bucket known`

- Aktiviere einen bekannten Eimer:

`scoop bucket add {{name}}`

- Aktiviere einen unbekannten Eimer durch die Angabe eines Namens und einer Git-Repository-URL:

`scoop bucket add {{name}} {{https://beispiel.de/repository.git}}`

- Deaktiviere einen Eimer:

`scoop bucket rm {{name}}`
