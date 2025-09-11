# mamba

> Fast, cross-platform package manager, intended as a drop-in replacement for conda.
> Some subcommands such as `repoquery` have their own usage documentation.
> More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- Create a new environment, installing the specified packages into it:

`mamba create {{[-n|--name]}} {{environment_name}} {{python=3.10 matplotlib}}`

- Install packages into the current environment, specifying the package channel:

`mamba install {{[-c|--channel]}} {{conda-forge}} {{python=3.6 numpy}}`

- Update all packages in the current environment:

`mamba update {{[-a|--all]}}`

- Search for a specific package across repositories:

`mamba repoquery search {{numpy}}`

- List all environments:

`mamba info {{[-e|--envs]}}`

- Remove unused packages and tarballs from the cache:

`mamba clean {{[-pt|--packages --tarballs]}}`

- Activate an environment:

`mamba activate {{environment_name}}`

- List all installed packages in the currently activated environment:

`mamba list`
