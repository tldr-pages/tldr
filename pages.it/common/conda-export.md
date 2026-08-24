# conda export

> Esporta i dettagli dell'ambiente.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/export.html>.

- Esporta i dettagli dell'ambiente corrente su `stdout`:

`conda export`

- Esporta i dettagli dell'ambiente corrente in un file `YAML`:

`conda export {{[-f|--file]}} {{percorso/a/environment.yaml}}`

- Esporta i dettagli in un formato specifico:

`conda export --format {{environment-json|environment-yaml|explicit|json|reqs|requirements|txt|yaml|yml}}`

- Seleziona un ambiente per nome:

`conda export {{[-n|--name]}} {{nome_ambiente}}`

- Seleziona un ambiente tramite il suo percorso:

`conda export {{[-p|--prefix]}} {{percorso/a/ambiente}}`

- Includi un canale specifico:

`conda export {{[-c|--channel]}} {{nome_canale}}`
