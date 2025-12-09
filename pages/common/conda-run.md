# conda run

> Run an executable command in a conda environment.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/run.html>.

- Run a command in the currently active environment:

`conda run {{command}}`

- Target an environment by name:

`conda run {{[-n|--name]}} {{environment_name}} {{command}}`

- Target an environment by its path (i.e. prefix):

`conda run {{[-p|--path]}} {{path/to/env}} {{command}}`
