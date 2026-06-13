# conda list

> List installed packages in a conda environment.
> More information: <https://docs.conda.io/projects/conda/en/stable/commands/list.html>.

- List all packages in the current environment:

`conda list`

- List packages in the named environment:

`conda list {{[-n|--name]}} {{environment}}`

- List packages installed in a given path:

`conda list {{[-p|--prefix]}} {{path/to/environment}}`

- Filter installed packages using `regex`:

`conda list {{regex}}`

- Save packages for future use:

`conda list {{[-e|--export]}} > {{path/to/package-list.txt}}`
