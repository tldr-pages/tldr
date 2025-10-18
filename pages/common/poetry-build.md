# poetry build

> Build a Poetry package as a tarball and a wheel.
> More information: <https://python-poetry.org/docs/cli/#build>.

- Build the package in the default format (sdist and wheel):

`poetry build`

- Build only the wheel package:

`poetry build --format {{wheel}}`

- Build only the source distribution (sdist):

`poetry build --format {{sdist}}`

- Build the package and output to a specific directory:

`poetry build --output {{path/to/directory}}`

- Display help:

`poetry build --help`
