# mitmdump

> Vizualizați, înregistrați și transformați prin programare traficul HTTP.
> Comotria de linie de comandă la mitmproxy.
> Mai multe informaţii: <https://docs.mitmproxy.org/stable/overview-tools/#mitmdump>

- Porniți un proxy și salvați toate ieșirile într-un fișier:

`mitmdump -w {{filename}}`

- Filtrați un fișier de trafic salvat la doar cereri POST:

`mitmdump -nr {{input_filename}} -w {{output_filename}} "{{~m post}}"`

- Reluarea unui fișier de trafic salvat:

`mitmdump -nc {{filename}}`
