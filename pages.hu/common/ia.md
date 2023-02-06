# ia

> Parancssoros eszköz a `archive.org`. További információ: <https://archive.org/services/docs/api/internetarchive/cli.html>.

- A `ia` beállítása API-kulcsokkal (egyes funkciók nem működnek e lépés nélkül):

`ia configure`

- Töltsön fel egy vagy több elemet a `archive.org`:

`ia upload {{identifier}} {{path/to/file}} --metadata="{{mediatype:data}}" --metadata="{{title:example}}"`

- Egy vagy több elem letöltése a `archive.org`:

`ia download {{item}}`

- Egy vagy több elem törlése a `archive.org`:

`ia delete {{identifier}} {{file}}`

- Keresés a `archive.org` oldalon, az eredmények JSON formátumban történő visszaküldése:

`ia search '{{subject:"subject" collection:collection}}'`
