# rake

> Een Make-achtig programma voor Ruby.
> Taken voor `rake` worden gespecificeerd in een Rakefile.
> Meer informatie: <https://ruby.github.io/rake/>.

- Voer de `default` Rakefile-taak uit:

`rake`

- Voer een specifieke taak uit:

`rake {{taak}}`

- Voer `n` taken tegelijk parallel uit (standaard aantal CPU-kernen + 4):

`rake --jobs {{n}}`

- Gebruik een specifieke Rakefile:

`rake --rakefile {{pad/naar/Rakefile}}`

- Voer `rake` uit vanuit een andere map:

`rake --directory {{pad/naar/map}}`
