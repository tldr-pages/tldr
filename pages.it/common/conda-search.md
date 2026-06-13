# conda search

> Cerca pacchetti e mostra i loro dettagli.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/search.html>.

- Cerca un pacchetto specifico:

`conda search {{nome_pacchetto}}`

- Cerca un pacchetto con i relativi dettagli:

`conda search {{nome_pacchetto}} {{[-i|--info]}}`

- Cerca pacchetti che contengono `stringa` nel nome:

`conda search "*stringa*"`

- Cerca una versione specifica di un pacchetto:

`conda search "{{nome_pacchetto}}>={{versione_pacchetto}}"`

- Cerca un pacchetto all'interno di un canale specifico:

`conda search {{canale}}::{{nome_pacchetto}}`

- Verifica se un pacchetto è installato in uno qualsiasi degli ambienti locali:

`conda search --envs {{nome_pacchetto}}`
