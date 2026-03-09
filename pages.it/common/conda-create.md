# conda create

> Crea nuovi ambienti conda.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Crea ambiente `py39` con Python 3.9, NumPy≥1.11, SciPy (sì a tutto):

`conda create {{[-ny|--name --yes]}} py39 python=3.9 "numpy>=1.11 scipy"`

- Crea `myenv` da file elenco pacchetti:

`conda create {{[-n|--name]}} myenv --file {{file1.yml}} --file {{file2.yml}}`

- Crea ambiente in percorso personalizzato:

`conda create {{[-p|--prefix]}} {{percorso/del/myenv}}`

- Clona ambiente `py39`:

`conda create --clone py39 {{[-n|--name]}} {{py39-copy}}`

- Aiuto:

`conda create {{[-h|--help]}}`
