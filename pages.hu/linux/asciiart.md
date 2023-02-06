# asciiart

> Képek átalakítása ASCII-be. További információ: <https://github.com/nodanaonlyzuul/asciiart>.

- Kép beolvasása egy fájlból és nyomtatása ASCII formátumban:

`asciiart {{path/to/image.jpg}}`

- Kép beolvasása egy URL-címről és nyomtatása ASCII-ben:

`asciiart {{www.example.com/image.jpg}}`

- Válassza ki a kimeneti szélességet (alapértelmezett érték 100):

`asciiart --width {{50}} {{path/to/image.jpg}}`

- Az ASCII kimenet színezése:

`asciiart --color {{path/to/image.jpg}}`

- Válassza ki a kimeneti formátumot (az alapértelmezett formátum szöveg):

`asciiart --format {{text|html}} {{path/to/image.jpg}}`

- Invertálja a karaktertérképet:

`asciiart --invert-chars {{path/to/image.jpg}}`
