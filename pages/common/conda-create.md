# conda create

> Create new conda environments.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>

- Create a new environment named py35 and install Python 3.5 and numpy at least 1.11 in it:

`conda create --yes --name py35 python=3.5 "numpy>=1.11"`

- Make exact copy of an environment:

`conda create --clone py35 --name py35-2`

- Create a new environment, name it bio-env and install the biopython package:

`conda create --name bio-env biopython`
