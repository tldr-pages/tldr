# paramspider

> Mine URLs with parameters from web archives.
> More information: <https://github.com/devanshbatham/ParamSpider>.

- Mine URLs with parameters for a specific [d]omain:

`paramspider {{[-d|--domain]}} {{example.com}}`

- Mine URLs for multiple domains from a [l]ist file:

`paramspider {{[-l|--list]}} {{path/to/domains.txt}}`

- Mine URLs and [s]tream the output to the terminal:

`paramspider {{[-d|--domain]}} {{example.com}} {{[-s|--stream]}}`

- Mine URLs using a custom [p]laceholder for parameter values:

`paramspider {{[-d|--domain]}} {{example.com}} {{[-p|--placeholder]}} "{{FUZZ}}"`

- Mine URLs through a proxy:

`paramspider {{[-d|--domain]}} {{example.com}} --proxy {{http://127.0.0.1:8080}}`
