# poetry build

> Build a Poetry package as a tarball and a wheel.
> More information: <https://python-poetry.org/docs/cli/#build>.

- Build a tarball and a wheel for the project:

`poetry build`

- Build a wheel package:

`poetry build {{[-f|--format]}} wheel`

- Build a source distribution (sdist):

`poetry build {{[-f|--format]}} sdist`

- Clean the output directory before building:

`poetry build --clean`

- Set the output directory:

`poetry build {{[-o|--output]}} {{path/to/directory}}`
