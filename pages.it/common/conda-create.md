# conda create

> Crea nuovi ambienti conda.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Crea un nuovo ambiente chiamato `py39`, installa Python 3.9, NumPy v1.11 o superiore e l'ultima versione stabile di SciPy. Conferma automaticamente tutte le richieste:

`conda create {{[-ny|--name --yes]}} py39 python=3.9 "numpy>=1.11 scipy"`

- Crea un nuovo ambiente chiamato `myenv` e installa i pacchetti elencati nei file specificati:

`conda create {{[-n|--name]}} myenv --file {{file1.yml}} --file {{file2.yml}}`

- Crea un nuovo ambiente in un percorso personalizzato (prefisso):

`conda create {{[-p|--prefix]}} {{percorso/al/myenv}}`

- Crea una copia esatta di un ambiente chiamato `py39`:

`conda create --clone py39 {{[-n|--name]}} {{py39-copy}}`

- Mostra l'aiuto:

`conda create {{[-h|--help]}}`
