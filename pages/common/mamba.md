# mamba

> The fast, cross-platform package manager, intended as a drop-in replacement for conda.
> Some subcommands such as `mamba repoquery` have their own usage documentation.
> More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- Create a new environment, installing the specified packages into it:

`mamba create --name {{environment_name}} {{python=3.10 matplotlib}}`

- List all environments:

`mamba info --envs`

- Activate an environment:

`mamba activate {{environment_name}}`

- Deactivate an environment:

`mamba {{deactivate}}`

- Delete an environment and remove all packages:

`mamba remove --name {{environment_name}} --all`

- List all installed packages in the currently activated environment:

`mamba list`

- Search for a particular package across repositories:

`mamba repoquery search {{numpy}}`

- Install packages into the current environment:

`mamba install {{python=3.6 numpy}}`
