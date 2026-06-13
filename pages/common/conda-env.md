# conda env

> Manage conda environments.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/env/index.html>.

- Create an environment from an environment file (YAML, TXT, etc.):

`conda env create {{[-f|--file]}} {{path/to/file}}`

- Delete an environment and everything in it:

`conda env remove {{[-n|--name]}} {{environment_name}}`

- Update an environment based on an environment file:

`conda env update {{[-f|--file]}} {{path/to/file}} --prune`

- List all environments:

`conda env list`

- View environment details:

`conda env export`

- List environment variables:

`conda env config vars list`

- Set environment variables:

`conda env config vars set {{my_var}}={{value}}`
