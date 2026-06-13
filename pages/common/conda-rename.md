# conda rename

> Rename an existing conda environment.
> The base environment and the currently-active environment cannot be renamed.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/rename.html>.

- Rename an environment via its name:

`conda rename {{[-n|--name]}} {{current_name}} {{new_name}}`

- Rename an environment via its full path (i.e. prefix):

`conda rename {{[-p|--prefix]}} {{path/to/env}} {{new_name}}`
