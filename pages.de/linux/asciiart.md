# asciiart

> Konvertiere Bilder zu ASCII.
> Mehr Informationen: <https://github.com/nodanaonlyzuul/asciiart>.

- Lese ein Bild aus einer Datei und zeige es als ASCII:

`asciiart {{pfad/zur/datei.jpg}}`

- Lese ein Bild aus einer URL und zeige es als ASCII:

`asciiart {{www.example.com/bild.jpg}}`

- Wähle die output Breite (default ist 100):

`asciiart -width {{50}} {{pfad/zum/bild.jpg}}`

- Zeige den output in Farbe:

`asciiart --color {{pfad/zum/bild.jpg}}`

- Wähle das output Format (default ist text):

`asciiart --format {{text|html}} {{pfad/zum/bild.jpg}}`

- Invertiere die Buchstaben Map:

`asciiart --invert-chars {{pfad/zum/bild.jpg}}`
