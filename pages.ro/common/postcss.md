# postcss

> PostCSS este un instrument pentru transformarea stilurilor cu plugin-uri JS.
> Mai multe informaţii: <https://postcss.org>

- analizarea și transformarea unui fișier CSS:

`postcss {{path/to/file}}`

- analiza și transformarea unui fișier CSS și ieșirea într-un anumit fișier:

`postcss {{path/to/file}} --output {{path/to/file}}`

- Parse și transforma un fișier CSS și de ieșire într-un anumit director:

`postcss {{path/to/file}} --dir {{path/to/directory}}`

- analizarea și transformarea unui fișier CSS în loc:

`postcss {{path/to/file}} --replace`

- Specificaţi un parser PostCSS personalizat:

`postcss {{path/to/file}} --parser {{parser}}`

- Specificaţi o sintaxă PostCSS personalizată:

`postcss {{path/to/file}} --syntax {{syntax}}`

- Urmăriți modificările la un fișier CSS:

`postcss {{path/to/file}} --watch`

- Afișați opțiunile și exemplele disponibile:

`postcss --help`
