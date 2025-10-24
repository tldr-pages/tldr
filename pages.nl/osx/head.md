# head

> Geef het eerste deel van bestanden weer.
> Meer informatie: <https://keith.github.io/xcode-man-pages/head.1.html>.

- Toon de eerste 10 regels van een bestand:

`head {{pad/naar/bestand}}`

- Toon de eerste 10 regels van meerdere bestanden:

`head {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon de eerste 5 regels van een bestand:

`head {{[-5|--lines 5]}} {{pad/naar/bestand}}`

- Geef de eerste paar regels van een bestand weer:

`head {{[-n|--lines]}} {{aantal}} {{pad/naar/bestand}}`

- Geef de eerste paar bytes van een bestand weer:

`head {{[-c|--bytes]}} {{aantal}} {{pad/naar/bestand}}`

- Geef alles behalve de laatste paar regels van een bestand weer:

`head {{[-n|--lines]}} -{{aantal}} {{pad/naar/bestand}}`

- Geef alles behalve de laatste paar bytes van een bestand weer:

`head {{[-c|--bytes]}} -{{aantal}} {{pad/naar/bestand}}`
