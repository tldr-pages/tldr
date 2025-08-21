# conda env

> Manage conda environments.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/env/index.html>.

- Create an environment from an environment file (yml, txt, etc):

`conda env create {{[-f|--file]}} {{file_name}}`

- Delete an environment and everything in it:

`conda env remove {{[-n|--name]}} {{environment_name}}`

- Update an environment based on an environment file:

`conda env update {{[-f|--file]}} {{file_name}} --prune`

- List all environments:

`conda env list`

- View environment details:

`conda env export`

- List environment variables:

`conda env config vars list`

- Set environment variables:

`conda env config vars set {{my_var=value}}`
