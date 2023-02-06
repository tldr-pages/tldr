# jp2a

> JPEG képek ASCII-be konvertálása. További információ: <https://csl.name/jp2a/>.

- JPEG kép beolvasása fájlból és nyomtatása ASCII formátumban:

`jp2a {{path/to/image.jpeg}}`

- JPEG-kép olvasása URL-címről és nyomtatás ASCII-ben:

`jp2a {{www.example.com/image.jpeg}}`

- Az ASCII kimenet színezése:

`jp2a --colors {{path/to/image.jpeg}}`

- Az ASCII-kimenethez használandó karakterek megadása:

`jp2a --chars='{{..-ooxx@@}}' {{path/to/image.jpeg}}`

- Az ASCII kimenet kiírása egy fájlba:

`jp2a --output={{path/to/output_file.txt}} {{path/to/image.jpeg}}`

- Az ASCII kimenet HTML fájlformátumba írása, amely alkalmas webböngészőkben való megjelenítésre:

`jp2a --html --output={{path/to/output_file.html}} {{path/to/image.jpeg}}`
