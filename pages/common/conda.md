# conda

> Package, dependency and environment management for any programming language.

- Create a new environment, installing named packages (eg. python=2.7):

`conda create --name {{environment_name}} {{packages}}`

- List all environments:

`conda info --envs`

- Load or unload an environment:

`source {{activate|deactivate}} {{environment_name}}`

- Delete an environment (remove all packages):

`conda remove --name {{environment_name}} --all`

- Search conda channels for a package by name:

`conda search {{package_name}}`

- Install one or more packages into the current environment:

`conda install {{packages}}`

- List currently installed packages in current environment:

`conda list`

- Delete unused packages and caches:

`conda clean --all`