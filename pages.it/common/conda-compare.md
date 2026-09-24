# conda compare

> Confronta i pacchetti tra ambienti conda.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/commands/compare.html>.

- Confronta i pacchetti nella directory corrente con quelli nel file `file.yml`:

`conda compare file.yml`

- Confronta i pacchetti nell'ambiente chiamato `myenv` con quelli nel file `file.yml`:

`conda compare {{[-n|--name]}} myenv {{percorso/a/file.yml}}`

- Confronta i pacchetti nell'ambiente `myenv` situato in un percorso personalizzato (prefisso) con quelli nel file `file.yml`:

`conda compare {{[-p|--prefix]}} {{percorso/a/myenv}} {{percorso/a/file.yml}}`

- Mostra l'aiuto:

`conda compare {{[-h|--help]}}`
