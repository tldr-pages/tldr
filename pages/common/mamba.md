# mamba

> Fast, cross-platform package manager, intended as a drop-in replacement for conda.
> Some subcommands such as `mamba repoquery` have their own usage documentation.
> More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- Create a new environment, installing the specified packages into it:

`mamba create --name {{environment_name}} {{python=3.10 matplotlib}}`

- Install packages into the current environment, specifying the package [c]hannel:

`mamba install -c {{conda-forge}} {{python=3.6 numpy}}`

- Update all packages in the current environment:

`mamba update --all`

- Search for a specific package across repositories:

`mamba repoquery search {{numpy}}`

- List all environments:

`mamba info --envs`

- Remove unused [p]ackages and [t]arballs from the cache:

`mamba clean -pt`

- Activate an environment:

`mamba activate {{environment_name}}`

- List all installed packages in the currently activated environment:

`mamba list`
