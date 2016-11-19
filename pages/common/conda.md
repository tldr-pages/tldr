# conda

> Package, dependency and environment management for any language.

- Create a new environment:

`conda create --name {{environment_name}} {{packages}}`

- List all environments:

`conda info --envs`

- Load an environment:

`source activate {{environment_name}}`

- Exit from an environment:

`source deactivate {{environment_name}}`

- Delete an environment:

`conda remove --name {{environment_name}} --all`

- Install one or more conda packages:

`conda install {{packages}}`

- Delete unused packages and caches:

`conda clean --all`