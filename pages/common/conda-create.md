# conda create

> Create new conda environments.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Create a new environment named `py39`, and install Python 3.9 and NumPy v1.11 or above in it:

`conda create --yes --name {{py39}} python={{3.9}} "{{numpy>=1.11}}"`

- Make exact copy of an environment:

`conda create --clone {{py39}} --name {{py39-copy}}`

- Create a new environment with a specified name and install a given package:

`conda create --name {{env_name}} {{package}}`
