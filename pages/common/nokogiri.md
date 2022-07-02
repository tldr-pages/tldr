# nokogiri

> An HTML, XML, SAX and Reader parser.
> More information: <https://nokogiri.org>.

- Parse the contents of a URL or file:

`nokogiri {{url|path/to/file}}`

- Parse as a specific type:

`nokogiri {{url|path/to/file}} --type {{xml|html}}`

- Load a specific initialization file before parsing:

`nokogiri {{url|path/to/file}} -C {{path/to/config_file}}`

- Parse using a specific encoding:

`nokogiri {{url|path/to/file}} --encoding {{encoding}}`

- Validate using a RELAX NG file:

`nokogiri {{url|path/to/file}} --rng {{url|path/to/file}}`
