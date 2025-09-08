# conda create

> Create new conda environments.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Create a new environment [n]amed `py39`, install Python 3.9, NumPy v1.11 or above in it, and the latest stable version of SciPy. Say [y]es to all confirmations:

`conda create {{[-ny|--name --yes]}} {{py39}} python={{3.9}} "{{numpy>=1.11 scipy}}"`

- Create a new environment [n]amed `myenv` and install packges listed in files:

`conda create {{[-n|--name]}} myenv --file {{file1.yml}} --file {{file2.yml}}`

- Create a new environment named `myenv` at custom [p]ath(i.e. [p]refix):

`conda create {{[-p|--prefix]}} {{/path/to/myenv}}`

- Make exact copy of an environment [n]amed `py39`:

`conda create --clone {{py39}} {{[-n|--name]}} {{py39-copy}}`

- Display detailed [h]elp message:

`conda create {{[-h|--help]}}`
