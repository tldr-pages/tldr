# nokogiri

> HTML, XML, SAX és Reader elemző. További információ: <https://nokogiri.org>.

- Egy URL vagy fájl tartalmának elemzése:

`nokogiri {{url|path/to/file}}`

- Elemzés egy adott típusként:

`nokogiri {{url|path/to/file}} --type {{xml|html}}`

- Egy adott inicializálófájl betöltése az elemzés előtt:

`nokogiri {{url|path/to/file}} -C {{path/to/config_file}}`

- Elemzés egy adott kódolással:

`nokogiri {{url|path/to/file}} --encoding {{encoding}}`

- Validálás RELAX NG fájl használatával:

`nokogiri {{url|path/to/file}} --rng {{url|path/to/file}}`
