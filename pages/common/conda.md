# conda

> Package, dependency and environment management for any programming language.
> Some subcommands such as `create` have their own usage documentation.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/index.html>.

- Create a new environment, installing named packages into it:

`conda create {{[-n|--name]}} {{environment_name}} {{python=3.9 matplotlib}}`

- List all environments:

`conda info {{[-e|--envs]}}`

- Load an environment:

`conda activate {{environment_name}}`

- Unload an environment:

`conda deactivate`

- Delete an environment (remove all packages):

`conda remove {{[-n|--name]}} {{environment_name}} --all`

- Install packages into the current environment:

`conda install {{python=3.4 numpy}}`

- List currently installed packages in current environment:

`conda list`

- Delete unused packages and caches:

`conda clean {{[-a|--all]}}`
