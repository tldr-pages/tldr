# poetry show

> Show details of packages in your Poetry project.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#show>.

- Display all packages:

`poetry show`

- Show details of a specific package:

`poetry show {{package_name}}`

- Show details as a dependency tree:

`poetry show {{[-t|--tree]}}`

- Only show top-level packages (those explicitly defined in `pyproject.toml`):

`poetry show {{[-T|--top-level]}}`

- Show outdated packages:

`poetry show {{[-o|--outdated]}}`

- Show the latest versions for all packages:

`poetry show {{[-l|--latest]}}`

- Exclude a specific dependency group/s:

`poetry show --without {{group1,group2,...}}`

- Only show a specific dependency group/s:

`poetry show --only {{group1,group2,...}}`
