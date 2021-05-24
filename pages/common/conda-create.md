# conda create

> Creates new conda environments. \
> Drawn from conda cheat sheet: \
> <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf> \
> Docs: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>

- Create a new environment named py35, install Python 3.5 and numpy at least 1.11 in it

`conda create --yes --name py35 python=3.5 "numpy>=1.11"`

- Make exact copy of an environment

`conda create --clone py35 --name py35-2`

- Create a new environment, name it bio-env and install the biopython package

`conda create --name bio-env biopython`
