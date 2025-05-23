# micromamba

> A fast, minimal, standalone package and environment manager for conda packages.
> Drop-in replacement for conda, ideal for CI, Docker, and lightweight setups.
> More information: <https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html>.

- Create a new environment at a specific path, installing named packages into it:

`micromamba create -p {{/path/to/env}} {{python=3.11 numpy}}`

- Create a new environment by name:

`micromamba create -n {{env_name}} {{python=3.11 matplotlib}}`

- Activate an environment by name or path:

`micromamba activate {{env_name}}`
`micromamba activate -p {{/path/to/env}}`

- Run a command inside an environment without activating it in the shell:

`micromamba run -n {{env_name}} {{python script.py}}`
`micromamba run -p {{/path/to/env}} {{pytest tests/}}`

- Install packages into the currently active environment:

`micromamba install {{scipy pandas}}`

- Update packages in the current environment:

`micromamba update {{package_name}}`

- Remove packages from the current environment:

`micromamba remove {{package_name}}`

- List all installed packages in the current environment:

`micromamba list`

- List all environments:

`micromamba env list`

- Search for packages in channels or current environment:

`micromamba search {{package_name}}`

- Query tree-like dependencies of a package:

`micromamba repoquery depends -t {{package_name}}`

- Clean unused packages and caches:

`micromamba clean --all`

- Generate shell init scripts for activation support (e.g., for bash):

`micromamba shell init -s {{bash}} -p {{~/.micromamba}}`

- Show information about the current micromamba setup:

`micromamba info`

- Update micromamba itself:

`micromamba self-update`
