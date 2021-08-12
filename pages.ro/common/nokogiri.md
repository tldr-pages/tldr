# nokogiri

> Un parser HTML, XML, SAX și Reader.
> Mai multe informaţii: <https://nokogiri.org>

- Analizați conținutul unui URL sau al unui fișier:

`nokogiri {{url|path/to/file}}`

- Parse ca un anumit tip:

`nokogiri {{url|path/to/file}} --type {{xml|html}}`

- Încărcați un fișier de inițializare specific înainte de analiză:

`nokogiri {{url|path/to/file}} -C {{path/to/config_file}}`

- Parse folosind o codificare specifică:

`nokogiri {{url|path/to/file}} --encoding {{encoding}}`

- Validează utilizând un fișier RELAX NG:

`nokogiri {{url|path/to/file}} --rng {{url|path/to/file}}`
