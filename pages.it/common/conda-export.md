# conda export

> Esporta dettagli ambiente.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/export.html>.

- Esporta ambiente corrente ('stdout'):

`conda export`

- Esporta in file YAML:

`conda export {{[-f|--file]}} {{percorso/dell/environment.yaml}}`

- Formato specifico:

`conda export --format {{environment-yaml|yaml|yml}}`

- Ambiente per nome:

`conda export {{[-n|--name]}} {{nome_ambiente}}`

- Ambiente per percorso:

`conda export {{[-p|--prefix]}} {{percorso/dell/ambiente}}`

- Canale specifico:

`conda export {{[-c|--channel]}} {{nome_canale}}`
