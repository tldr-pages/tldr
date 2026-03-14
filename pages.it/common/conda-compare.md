# conda compare

> Confronta pacchetti tra ambienti conda.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/commands/compare.html>.

- Confronta pacchetti directory corrente con `file.yml`:

`conda compare file.yml`

- Confronta ambiente `myenv` con `file.yml`:

`conda compare {{[-n|--name]}} myenv {{percorso/del/file.yml}}`

- Confronta ambiente `myenv` da percorso con `file.yml`:

`conda compare {{[-p|--prefix]}} {{percorso/del/myenv}} {{percorso/del/file.yml}}`

- Aiuto:

`conda compare {{[-h|--help]}}`
