# asciiart

> Conversia imaginilor în ASCII.
> Mai multe informaţii: <https://github.com/nodanaonlyzuul/asciiart>

- Citiți o imagine dintr-un fișier și imprimați în ASCII:

`asciiart {{path/to/image.jpg}}`

- Citiți o imagine dintr-un URL și imprimați în ASCII:

`asciiart {{www.example.com/image.jpg}}`

- Alegeți lățimea de ieșire (implicit este 100):

`asciiart -width {{50}} {{path/to/image.jpg}}`

- Colorizează ieșirea ASCII:

`asciiart --color {{path/to/image.jpg}}`

- Alegeți formatul de ieșire (formatul implicit este text):

`asciiart --format {{text|html}} {{path/to/image.jpg}}`

- Inversează harta caracterelor:

`asciiart --invert-chars {{path/to/image.jpg}}`
