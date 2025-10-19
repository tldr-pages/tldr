# poetry add

> Add dependencies to the current Poetry project.
> More information: <https://python-poetry.org/docs/cli/#add>.

- Add the latest compatible version of a package:

`poetry add {{package}}`

- Add a package with a version constraint:

`poetry add {{package}}@{{^1.2}}`

- Add a package to a group (for example, "dev"):

`poetry add --group {{dev}} {{package}}`

- Add one or more optional extras from a package:

`poetry add {{package}} -E {{extra1}} -E {{extra2}}`

- Add a package directly from a Git repository:

`poetry add git+https://github.com/{{user}}/{{repo}}.git`

- Add a package from a local path:

`poetry add {{path/to/local_package}}`
