# conda create

> Create new conda environments.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Create a new environment named `py39`, install Python 3.9, NumPy v1.11 or above in it, and the latest stable version of SciPy. Say yes to all confirmations:

`conda create {{[-ny|--name --yes]}} {{py39}} python={{3.9}} "{{numpy>=1.11 scipy}}"`

- Create a new environment named `myenv` and install packages listed in files:

`conda create {{[-n|--name]}} myenv --file {{file1.yml}} --file {{file2.yml}}`

- Create a new environment named `myenv` at custom path (i.e. prefix):

`conda create {{[-p|--prefix]}} {{path/to/myenv}}`

- Make exact copy of an environment named `py39`:

`conda create --clone py39 {{[-n|--name]}} {{py39-copy}}`

- Display help:

`conda create {{[-h|--help]}}`
