# conda create

> Create new conda environments.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Create a new environment named py39 and install Python 3.9 and numpy at least 1.11 in it:

`conda create --yes --name {{py39}} python={{3.9}} "{{numpy>=1.11}}"`

- Make exact copy of an environment:

`conda create --clone {{py39}} --name {{py39-copy}}`

- Create a new environment, name it bio-env and install the biopython package:

`conda create --name {{bio-env}} {{biopython}}`
