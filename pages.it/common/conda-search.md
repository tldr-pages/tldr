# conda search

> Cerca pacchetti e dettagli.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/search.html>.

- Cerca pacchetto:

`conda search {{pacchetto}}`

- Dettagli pacchetto:

`conda search {{pacchetto}} {{[-i|--info]}}`

- Stringa nel nome:

`conda search "*stringa*"`

- Versione specifica:

`conda search "{{pacchetto}}>=versione"`

- Canale specifico:

`conda search {{canale}}::{{pacchetto}}`

- Ambienti locali:

`conda search --envs {{pacchetto}}`
