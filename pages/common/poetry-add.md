# poetry add

> Add required packages to the `pyproject.toml` file in Poetry.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#add>.

- Add required packages:

`poetry add {{package_name}}`

- Add required packages to a specific group of dependencies:

`poetry add {{package_name}} --group {{group_name}}`

- Add a specific version of a package:

`poetry add {{package_name}}=={{version}}`

- Add a specific version of a package equal to or earlier than a given version:

`poetry add {{package_name}}<={{version}}`

- Add a specific version of a package equal to or later than a given version:

`poetry add {{package_name}}>={{version}}`
