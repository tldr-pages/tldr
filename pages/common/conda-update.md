# conda update

> Update packages within a conda environment, including conda itself.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/update.html>.

- Update all packages in the current environment:

`conda update {{[--all|--update-all]}}`

- Update a specific package in the current environment:

`conda update {{package_name}}`

- Update conda itself in the base environment:

`conda update {{[-n|--name]}} base conda`

- Update packages while ignoring pinned packages:

`conda update --no-pin`

- Update packages in offline mode:

`conda update --offline`
