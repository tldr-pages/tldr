# conda remove

> Remove packages from a conda environment.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/remove.html>.

- Remove `scipy` from the currently active environment:

`conda remove scipy`

- Remove a list of packages from the specified environment:

`conda remove {{[-n|--name]}} {{environment_name}} {{package1 package2 ...}}`

- Remove all packages and the environment itself:

`conda remove {{[-n|--name]}} {{environment_name}} --all`

- Remove all packages, but keep the environment:

`conda remove {{[-n|--name]}} {{environment_name}} --all --keep-env`
